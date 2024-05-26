import React, {useEffect, useState} from 'react';
import Swal from 'sweetalert2'

const FormComponent = () => {
  const [showForm, setShowForm] = useState(false);
  const [showResenia, setShowResenia] = useState(false)
  const [fechaDesde, setFechaDesde] = useState<string>()
  const [fechaHasta, setFechaHasta] = useState<string>()

  const [tipoDeVisualizacion, setTipoDeVisualizacion] = useState<string>()
  const [tipoDeResenia, setTipoDeResenia] = useState<string>()

    const tipoReseniaOptions = [
    { value: 'sommelier', label: 'Sommelier' },
    { value: 'normales', label: 'Normales' },
    { value: 'amigos', label: 'Amigos' },
  ];

  const tipoVisualizacionOptions = [
    { value: 'excel', label: 'Excel' },
    { value: 'pantalla', label: 'Pantalla' },
    { value: 'pdf', label: 'PDF' },
  ];

  const toggleForm = () => {
    setShowForm(!showForm);
  };
  const validarFechas = (fechaDesde: string, fechaHasta: string) => {
      return fechaDesde <= fechaHasta
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const validacion = validarFechas(fechaDesde!, fechaHasta!)

      if (!validacion) {
          Swal.fire({
              icon: "error",
              title: "Oops...",
              text: "fecha desde mayor a fecha hasta",
          });
          return
      }

    const data = {
        fecha_desde: fechaDesde,
        fecha_hasta: fechaHasta,
        tipo_de_resenia: tipoDeResenia,
        tipo_de_visualizacion: tipoDeVisualizacion,
    };
      console.log(data)

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
  };
    useEffect(() => {
        setShowResenia(fechaHasta !== undefined)
    }, [fechaHasta]);

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
            {/*  todo: validar las fechas antes de mostrar este cuadro */}
            {showResenia && (
              <div className="mb-3">
                <label className="form-label">Tipo de reseña:</label>
                <select
                  className="form-control"
                  onChange={e => setTipoDeResenia(e.target.value)}
                >
                  {tipoReseniaOptions.map(option => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
                <label className="form-label">Tipo de visualización:</label>
                <select
                  className="form-control"
                  onChange={e => setTipoDeVisualizacion(e.target.value)}
                >
                  {tipoVisualizacionOptions.map(option => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </div>
            )}

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
