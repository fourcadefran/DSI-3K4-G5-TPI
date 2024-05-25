import React, { useState } from 'react';

const FormComponent = () => {
  const [showForm, setShowForm] = useState(false);
  const [fechaDesde, setFechaDesde] = useState<string>()
  const [fechaHasta, setFechaHasta] = useState<string>()

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = {
      fecha_desde: fechaDesde,
      fecha_hasta: fechaHasta,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/ranking', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error('Error:', error);
    }
    console.log("ya mando todo!")
    // TODO: mandar todo al backend
  };

  return (
    <div className="d-flex align-items-center justify-content-center min-vh-100 bg-light">
      <div className="bg-white p-5 rounded shadow-lg">
        {!showForm ? (
          <button
            onClick={toggleForm}
            className="btn btn-primary"
          >
            Generar Ranking de Vinos
          </button>
        ) : (
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Fecha Desde:</label>
              <input
                type="date"
                className="form-control"
                onChange={ e => setFechaDesde(e.target.value)}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Fecha Hasta:</label>
              <input
                type="date"
                className="form-control"
                onChange={ e => setFechaHasta(e.target.value)}
              />
            </div>
            <div className="d-flex justify-content-between">
              <button
                type="button"
                onClick={toggleForm}
                className="btn btn-secondary"
              >
                Cancelar
              </button>
              <button
                type="submit"
                className="btn btn-success"
              >
                Enviar
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};

export default FormComponent;
