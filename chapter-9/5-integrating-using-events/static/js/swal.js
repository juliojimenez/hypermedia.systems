function sweetConfirm(elt, config) {
  Swal.fire(config).then((result) => {
    if (result.isConfirmed) {
      elt.dispatchEvent(new Event("confirmed"));
    }
  });
}
