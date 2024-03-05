<template>
<div>
  <div class="thumbnail" @click="openModal(id)">
    <div class="caption">
      {{ nom }}
    </div>
    <img :src="id +'.jpg'"/>
  </div> 

  <div :id="id" class="modal">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="box">
          <div class="card">
            <div class="card-image">
              <figure class="image is-4by3">
                <img :src="id +'.jpg'">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                </div>
                <div class="media-content">
                  <p class="title is-4"> {{ nom }} </p>
                  <p class="subtitle is-6"> {{ adresse }}, {{ ville }} </p>
                </div>
              </div>

              <div class="content">
                <div v-for="item in type" :key="item" id="types"> ~ {{ item }} ~ </div>
                <br>
                <a :href="'https://www.google.com/search?q=' + nom" target="_blank">Lien vers Google</a>
              </div>
            </div>
          </div>
      </div>
      </div>
      <button type="button" class="modal-close is-large" aria-label="close" @click="closeModal(id)"></button>
    </div> 
</div>          
</template>



<script>

export default {
  name: 'placeCard',
  components: {
    
  },
  props: {
    id: String,
    nom: String, 
    photo: String, 
    type: Array, 
    adresse: String,
    ville: String, 
    long: String,
    lat: String
  },
  methods: {
    openModal(id) {
      console.log(id)
      document.getElementById(id).classList.add("is-active");
    },
    closeModal(id) {
      document.getElementById(id).classList.remove("is-active");
    }
 }
}
</script>


<style>

img {
    display: block;
    height:400px;
    width:400px;
    object-fit: cover;
}

.thumbnail:hover {
  opacity: 0.5;
  cursor: pointer;
}

.thumbnail {
    position: relative;
    display: inline-block;
}

.caption {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50% );
    text-align: center;
    color: white;
    font-weight: bold;
    background-color: #454545; 
}

#types {
  display: inline;
}

</style>