import React, { useState, useEffect } from "react";
import axios from "axios";
import Swal from "sweetalert2";

const UserTable = () => {
  const [data, setData] = useState([]);
  const [editingUser, setEditingUser] = useState(null);
  const [formData, setFormData] = useState({ name: "", surname: "", email: "" });
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);

  const API_URL = "http://127.0.0.1:8000/users/api/";

  const fetchUsers = () => {
    axios
      .get(API_URL)
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const refreshToken = async () => {
    const refresh = localStorage.getItem("refreshToken");
    if (!refresh) return null;
    try {
      const response = await axios.post("http://127.0.0.1:8000/users/token/refresh/", {
        refresh,
      });
      localStorage.setItem("accessToken", response.data.access);
      return response.data.access;
    } catch {
      return null;
    }
  };

  const handleDelete = async (userId, userEmail) => {
    const currentEmail = localStorage.getItem("userEmail");
    if (userEmail === currentEmail) {
      Swal.fire("⚠️", "No puedes eliminarte a ti mismo", "warning");
      return;
    }

    const confirm = await Swal.fire({
      title: "¿Estás seguro?",
      text: "No podrás revertir esto",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar",
    });

    if (confirm.isConfirmed) {
      let accessToken = localStorage.getItem("accessToken");

      try {
        await axios.delete(`${API_URL}${userId}/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        Swal.fire("¡Eliminado!", "El usuario fue eliminado con éxito", "success");
        fetchUsers();
      } catch {
        accessToken = await refreshToken();
        if (accessToken) {
          try {
            await axios.delete(`${API_URL}${userId}/`, {
              headers: {
                Authorization: `Bearer ${accessToken}`,
              },
            });
            Swal.fire("¡Eliminado!", "El usuario fue eliminado con éxito", "success");
            fetchUsers();
          } catch {
            Swal.fire("Error", "No se pudo eliminar el usuario", "error");
          }
        } else {
          Swal.fire("Error", "Sesión expirada. Vuelve a iniciar sesión", "error");
        }
      }
    }
  };

  const handleEdit = (user) => {
    setEditingUser(user);
    setFormData({
      name: user.name,
      surname: user.surname,
      email: user.email,
      age: user.age,             
      control_number: user.control_number, 
      tel: user.tel,              
    });
    setShowModal(true); 
  };

  const handleUpdate = async () => {
    const confirm = await Swal.fire({
      title: "¿Actualizar usuario?",
      icon: "question",
      showCancelButton: true,
      confirmButtonText: "Actualizar",
    });

    if (!confirm.isConfirmed) return;

    let accessToken = localStorage.getItem("accessToken");

    const updateUser = async (token) => {
      await axios.put(`${API_URL}${editingUser.id}/`, formData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
    };

    try {
      await updateUser(accessToken);
      Swal.fire("¡Actualizado!", "El usuario fue actualizado", "success");
      fetchUsers();
      setShowModal(false);
    } catch (error) {
      if (
        error.response?.data?.code === "token_not_valid" ||
        error.response?.status === 401
      ) {
        const newAccessToken = await refreshToken();
        if (newAccessToken) {
          try {
            await updateUser(newAccessToken);
            Swal.fire("¡Actualizado!", "El usuario fue actualizado", "success");
            fetchUsers();
            setShowModal(false);
          } catch (e) {
            console.error("Error luego de refrescar token:", e);
            Swal.fire("Error", "No se pudo actualizar el usuario", "error");
          }
        } else {
          Swal.fire("Sesión expirada", "Vuelve a iniciar sesión", "error");
        }
      } else {
        console.error("Error al actualizar:", error.response?.data || error);
        Swal.fire("Error", "No se pudo actualizar el usuario", "error");
      }
    }
  };

  if (loading) return <p>Cargando usuarios...</p>;

  return (
    <div className="container mt-5">
      <h2>Lista de Usuarios</h2>
      <table className="table table-striped mt-3">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {data.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
              <td>{user.surname}</td>
              <td>{user.email}</td>
              <td>
                <button
                  className="btn btn-warning me-2"
                  onClick={() => handleEdit(user)}
                >
                  <i className="bi bi-pencil"></i>
                </button>
                <button
                  className="btn btn-danger"
                  onClick={() => handleDelete(user.id, user.email)}
                >
                  <i className="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

     
      {showModal && (
        <div className="modal fade show d-block" tabIndex="-1" role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Actualizar usuario</h5>
                <button
                  type="button"
                  className="btn-close"
                  onClick={() => setShowModal(false)}
                ></button>
              </div>
              <div className="modal-body">
                <div className="form-group mt-2">
                  <label>Nombre</label>
                  <input
                    className="form-control"
                    type="text"
                    value={formData.name}
                    onChange={(e) =>
                      setFormData({ ...formData, name: e.target.value })
                    }
                  />
                </div>
                <div className="form-group mt-2">
                  <label>Apellido</label>
                  <input
                    className="form-control"
                    type="text"
                    value={formData.surname}
                    onChange={(e) =>
                      setFormData({ ...formData, surname: e.target.value })
                    }
                  />
                </div>
                <div className="form-group mt-2">
                  <label>Email</label>
                  <input
                    className="form-control"
                    type="email"
                    value={formData.email}
                    onChange={(e) =>
                      setFormData({ ...formData, email: e.target.value })
                    }
                  />
                </div>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowModal(false)}
                >
                  Cancelar
                </button>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={handleUpdate}
                >
                  Actualizar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Backdrop */}
      {showModal && (
        <div className="modal-backdrop fade show"></div>
      )}
    </div>
  );
};

export default UserTable;
