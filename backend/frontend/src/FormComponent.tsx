import { useState } from 'react';

const FormComponent = () => {
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };
  const handleSubmit = () => {
      //todo: mandar todo al backend
      fetch(BACEKDN )
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-lg">
        {!showForm ? (
          <button
            onClick={toggleForm}
            className="bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-700"
          >
            Generar Ranking de Vinos
          </button>
        ) : (
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div>
              <label className="block text-gray-700">Fecha Desde:</label>
              <input
                type="date"
                className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              />
            </div>
            <div>
              <label className="block text-gray-700">Fecha Hasta:</label>
              <input
                type="date"
                className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              />
            </div>
            <div className="flex justify-between">
              <button
                type="button"
                onClick={toggleForm}
                className="bg-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-700"
              >
                Cancelar
              </button>
              <button
                type="submit"
                className="bg-green-500 text-white py-2 px-4 rounded-lg hover:bg-green-700"
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
