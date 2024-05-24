import { useState } from 'react'

function App() {
  const [rankingButton, setRankingButton] = useState(false)
  const handleClick = () => {
      setRankingButton(true)
  }
  return (
    <>
        <button onClick={handleClick}>Generar Ranking de Vinos</button>
        { rankingButton && (
            <>
            {/* todo: form para ingresar datos*/}
            </>
        )}
    </>
  )
}

export default App
