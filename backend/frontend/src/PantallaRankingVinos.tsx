import React, { useEffect, useState } from "react"
import Swal from "sweetalert2"
import { Modal, Button } from "react-bootstrap"

interface Reporte {
  message: string
  reporte: object
}
const PantallaRankingVinos = () => {
  const [showForm, setShowForm] = useState(false)
  const [showResenia, setShowResenia] = useState(false)
  const [fechaDesde, setFechaDesde] = useState<string>()
  const [fechaHasta, setFechaHasta] = useState<string>()
  const [reporte, setReporte] = useState<Reporte>()
  const [showModal, setShowModal] = useState(false)

  const [tipoDeVisualizacion, setTipoDeVisualizacion] = useState<string>()
  const [tipoDeResenia, setTipoDeResenia] = useState<string>()

  const tipoReseniaOptions = [
    { value: "sommelier", label: "Sommelier" },
    { value: "normales", label: "Normales" },
    { value: "amigos", label: "Amigos" },
  ]

  const tipoVisualizacionOptions = [
    { value: "excel", label: "Excel" },
    { value: "pantalla", label: "Pantalla" },
    { value: "pdf", label: "PDF" },
  ]

  const toggleForm = () => {
    setShowForm(!showForm)
  }
  const validarFechas = (fechaDesde: string, fechaHasta: string) => {
    return fechaDesde <= fechaHasta
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    const validacion = validarFechas(fechaDesde!, fechaHasta!)

    if (!validacion) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "fecha desde mayor a fecha hasta",
      })
      return
    }

    if (tipoDeResenia === "normales" || tipoDeResenia === "amigos") {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: `El tipo de reseña "${tipoDeResenia}" no esta disponible`,
      })
      return
    }

    const data = {
      fecha_desde: fechaDesde,
      fecha_hasta: fechaHasta,
      tipo_de_resenia: tipoDeResenia,
      tipo_de_visualizacion: tipoDeVisualizacion,
    }
    console.log(data)

    try {
      const response = await fetch("http://127.0.0.1:8000/ranking", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })

      const result = await response.json()
      setReporte(result)
      setShowModal(true)
    } catch (error) {
      console.error("Error:", error)
    }
  }
  useEffect(() => {
    setShowResenia(fechaHasta !== undefined)
  }, [fechaHasta])

  return (
    <div className="d-flex align-items-center justify-content-center min-vh-100 bg-light">
      <div className="bg-white p-5 rounded shadow-lg">
        {!showForm ? (
          <button onClick={toggleForm} className="btn btn-primary">
            Generar Ranking de Vinos
          </button>
        ) : (
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Fecha Desde:</label>
              <input
                type="date"
                className="form-control"
                onChange={(e) => setFechaDesde(e.target.value)}
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Fecha Hasta:</label>
              <input
                type="date"
                className="form-control"
                onChange={(e) => setFechaHasta(e.target.value)}
              />
            </div>
            {/*  todo: validar las fechas antes de mostrar este cuadro */}
            {showResenia && (
              <div className="mb-3">
                <label className="form-label">Tipo de reseña:</label>
                <select className="form-control" onChange={(e) => setTipoDeResenia(e.target.value)}>
                  {tipoReseniaOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
                <label className="form-label">Tipo de visualización:</label>
                <select
                  className="form-control"
                  onChange={(e) => setTipoDeVisualizacion(e.target.value)}
                >
                  {tipoVisualizacionOptions.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </div>
            )}

            <div className="d-flex justify-content-between">
              <button type="button" onClick={toggleForm} className="btn btn-secondary">
                Cancelar
              </button>
              <button type="submit" className="btn btn-success">
                Confirmar
              </button>
            </div>
          </form>
        )}
      </div>
      <Modal show={showModal} onHide={() => setShowModal(false)} size="lg">
        <Modal.Header closeButton>
          <Modal.Title>Reporte de Vinos</Modal.Title>
        </Modal.Header>
        <Modal.Body style={{ maxHeight: "70vh", overflowY: "auto" }}>
          {reporte ? (
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Calificación</th>
                  <th>Precio (ARS)</th>
                  <th>Bodega</th>
                  <th>Varietal</th>
                  <th>Región</th>
                  <th>País</th>
                </tr>
              </thead>
              <tbody>
                {/*@ts-expect-error*/}
                {reporte.reporte.map((item, index) => (
                  <tr key={index}>
                    <td>{item.nombre}</td>
                    <td>{item.calificacion.toFixed(2)}</td>
                    <td>{item.precio}</td>
                    <td>{item.bodega}</td>
                    <td>{item.varietal}</td>
                    <td>{item.region}</td>
                    <td>{item.pais}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No hay datos para mostrar.</p>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowModal(false)}>
            Cerrar
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  )
}

export default PantallaRankingVinos
