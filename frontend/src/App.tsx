import { useState } from 'react'

function App() {
  const [longLink, setLongLink] = useState('')
  const [shortLink, setShortLink] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [copied, setCopied] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setShortLink('')
    setCopied(false)

    if (!longLink.trim()) {
      setError('Вставь ссылку')
      return
    }

    try {
      new URL(longLink)
    } catch {
      setError('Невалидная ссылка')
      return
    }

    setLoading(true)

    try {
      const res = await fetch('/api/sendLongLink/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ long_link: longLink.trim() }),
      })

      if (!res.ok) {
        throw new Error(`Ошибка сервера: ${res.status}`)
      }

      const data = await res.json()

      // бэк возвращает только код, например: "abc12" или { short_code: "abc12" }
      const code =
        typeof data === 'string'
          ? data
          : data.short_code

      if (!code) {
        throw new Error('Бэк не вернул короткий код')
      }

      const short = `http://127.0.0.1:8000/${code}`
      setShortLink(short)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Что-то пошло не так')
    } finally {
      setLoading(false)
    }
  }

  const copyToClipboard = () => {
    if (!shortLink) return
    navigator.clipboard.writeText(shortLink)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-4">
      <div className="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 space-y-6">
        <h1 className="text-3xl font-bold text-center text-gray-900 dark:text-white">
          Сократи ссылку
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="url"
            value={longLink}
            onChange={(e) => setLongLink(e.target.value)}
            placeholder="Вставь длинную ссылку сюда..."
            className="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            autoFocus
            required
          />

          <button
            type="submit"
            disabled={loading}
            className={`
              w-full py-3 px-4 rounded-lg font-medium text-white 
              ${loading 
                ? 'bg-gray-400 cursor-not-allowed' 
                : 'bg-blue-600 hover:bg-blue-700 active:bg-blue-800'}
              transition-colors duration-200
            `}
          >
            {loading ? 'Сокращаем...' : 'Сократить'}
          </button>
        </form>

        {error && (
          <p className="text-red-600 dark:text-red-400 text-center font-medium">
            {error}
          </p>
        )}

        {shortLink && (
          <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg break-all text-center space-y-3">
            <p className="text-sm text-gray-600 dark:text-gray-300">
              Твоя короткая ссылка:
            </p>
            <a
              href={shortLink}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 dark:text-blue-400 hover:underline font-medium"
            >
              {shortLink}
            </a>

            <button
              onClick={copyToClipboard}
              className={`
                mt-2 px-4 py-2 rounded-lg text-sm font-medium
                ${copied 
                  ? 'bg-green-600 text-white' 
                  : 'bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-500'}
                transition-colors
              `}
            >
              {copied ? 'Скопировано!' : 'Скопировать'}
            </button>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
