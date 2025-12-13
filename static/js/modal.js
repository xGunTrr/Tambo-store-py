document.addEventListener("DOMContentLoaded", function() {
  const modalAgregar = document.getElementById("modalAgregarProducto");
  const modalEditar = document.getElementById("modalEditarProducto");
  const openBtn = document.querySelector(".agregar-btn");
  const closeBtn = document.getElementById("closeModal");
  const closeEditBtn = document.getElementById("closeModalEditar");
  const editarBotones = document.querySelectorAll(".btn-editar-producto");

  // Abrir modal de agregar
  openBtn.addEventListener("click", function() {
    modalAgregar.style.display = "flex";
  });

  // Cerrar modal de agregar
  closeBtn.addEventListener("click", function() {
    modalAgregar.style.display = "none";
  });

  // Cerrar modal de editar
  closeEditBtn.addEventListener("click", function() {
    modalEditar.style.display = "none";
  });

  // Abrir modal de editar con datos
  editarBotones.forEach(function(boton) {
    boton.addEventListener("click", function() {
      const id = this.getAttribute("data-id");
      const nombre = this.getAttribute("data-nombre");
      const categoria = this.getAttribute("data-categoria");
      const subcategoria = this.getAttribute("data-subcategoria");
      const precio = this.getAttribute("data-precio");
      const stock = this.getAttribute("data-stock");

      // Llenar el modal con los datos
      document.getElementById("edit_id").value = id;
      document.getElementById("edit_nombre").value = nombre;
      document.getElementById("edit_categoria").value = categoria;
      document.getElementById("edit_subcategoria").value = subcategoria;
      document.getElementById("edit_precio").value = precio;
      document.getElementById("edit_stock").value = stock;

      // Mostrar el modal
      modalEditar.style.display = "flex";
    });
  });

  // Cerrar si se hace clic fuera del contenido
  window.addEventListener("click", function(e) {
    if (e.target === modalAgregar) {
      modalAgregar.style.display = "none";
    }
    if (e.target === modalEditar) {
      modalEditar.style.display = "none";
    }
  });
});
