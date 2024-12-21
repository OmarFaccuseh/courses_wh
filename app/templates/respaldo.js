
<script>/*
    document.addEventListener('DOMContentLoaded', ()=>{
        const cursoData = document.getElementById('curso');
        const logueado = cursoData.getAttribute('data-loguado');

        const popup = document.getElementById("mypopup");
        const closePopup = document.getElementById("closepopup");

        let btn = document.getElementById('suscribir')
        btn.onclick = () => {
            if (logueado){
                fetch('{% url "suscribir" %}?curso_id='+encodeURIComponent('{{curso.id}}'))
                .then(res => res.json())
                .then(data => {
                    console.log('data rec: ', data)
                    if(data.ok){
                        btn.innerHTML = 'Suscrito'
                    }

                })
            }
            else {
               popup.classList.remove("hidden");
            }
        }

        // Close popup
        closePopup.addEventListener("click", () => {
            popup.classList.add("hidden");
        });
        
    })*/
</script>