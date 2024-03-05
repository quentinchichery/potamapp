<template>
<div>
  <div id="header">
     <!-- class="columns is-desktop"
    <div id="img_header_box" class="column is-two-thirds-tablet"> -->
        <!-- <img id="img_header" src="../../public/undraw_eating_together_re_ux62(1).svg"/> -->
      <!-- </div> -->
      <div id="header_txt_box" >
       <!-- class="column"  -->
        <div id="header_txt">
          Nos Adresses Parisiennes Préférées 🖤
          <div id="legend_header">
          🍫🍜🍒 <br>
          <a href="https://www.instagram.com/camilledrs" target="_blank">@camilledrs</a> <br>
          <a href="https://www.instagram.com/quentinchichery" target="_blank">@quentinchichery</a> 
        </div>
        </div>
      </div>
  </div>

  <form method="post" @change.prevent="searchPlaces" class="columns" id="form">
    <div id="form_grid" class="column is-one-quarter-desktop is-one-third-tablet">
      <div id="form_left">
        <div class="form_title container">
          Filtrer par envie
        </div>

<div class="button_box">
      <button type="button" class="button" @click="setContentTypes">👇🏻</button>
      </div>

      <div v-show='contentVisibleTypes'>
        <div class="type_scroll container" >
          <div v-for="item in types" v-bind:key="item" class="scroll_items">
              <input :value="item" type="checkbox" :name="item" :id="item" v-model="selectedType">
              <label :for="item">{{item}}</label>
          </div>
      </div>
      </div>
    </div>

      <div id="form_right">
        <div class="form_title container">
          Filtrer par quartier
        </div>
      
      <div class="button_box">
        <button type="button" class="button" @click="setContentArrondissements">👇🏻</button>
      </div>

      <div v-show='contentVisibleArrondissements'>
        <div class="type_scroll container">
          <div v-for="item in villes" v-bind:key="item" class="scroll_items">
              <input :value="item" type="checkbox" :name="item" :id="item" v-model="selectedCity">
              <label :for="item">{{item}}</label>
          </div>
          </div>
      </div>
    </div>

  </div>

      <div id="scroll_right" class="column">
        <div>
          <tag-input 
            :types='selectedType' @clicked="onClickTagType">
          </tag-input>
          <tag-input 
            :types='selectedCity' @clicked="onClickTagVille">
          </tag-input>
          </div>
          <div id="grid_places" >

              <div v-for= "place in Places" v-bind:key="place">
                <placeCard 
                  :id="place.id.toString()"
                  :nom='place.nom' 
                  :photo='place.photo'
                  :type='place.type'
                  :adresse='place.adresse'
                  :ville='place.ville'
                  :long='place.Long'
                  :lat='place.Lat'
                  >
                  </placeCard>
              </div>
          </div>  
          </div>
</form>
</div>
</template>

<script>
import placeCard from './placeCard.vue'
import TagInput from './TagInput.vue'
import axios from 'axios'

export default {
  name: 'MainPage',
  components: {
    placeCard,
    TagInput
  },
  props: {},
  data() {
    return {
        selectedType: ["coeur"], 
        selectedCity: [],
        types : ["coeur", "neobistrot","brunch","brasserie","gastronomique","pouce","vege","boulangerie","coffee","primeur","poissonerie","boucherie","cremerie","epicerie","patisserie","vins","burger","orient","crepes","italien","asiatique","glace","africain","indien","grec", "latino", "bar","the", "chocolatier"],
        villes : ["75001","75002","75003","75004","75005","75006","75007","75008","75009","75010","75011","75012","75013","75014","75015","75016","75017","75018","75019","75020"],
        Places: [], 
        contentVisibleArrondissements: true,
        contentVisibleTypes: true
      }
    }, 
    methods: {
      searchPlaces() {
          console.log({"Type" : this.selectedType, "Ville" : this.selectedCity})
          axios.post('https://europe-west1-potamapp.cloudfunctions.net/function-1', {"type" : this.selectedType, "ville" : this.selectedCity}) 
              .then((res) => {
                  console.log(res.data)
                  this.Places = JSON.parse(res.data)
                  })
              },
    onClickTagType (index) {
      this.selectedType.splice(index, 1)
      this.searchPlaces()
    },
    onClickTagVille (index) {
        this.selectedCity.splice(index, 1)
        this.searchPlaces()
    },
    setContentArrondissements() {
              this.contentVisibleArrondissements = !this.contentVisibleArrondissements
            },
    setContentTypes() {
              this.contentVisibleTypes = !this.contentVisibleTypes
            }
    },
    mounted() {
      this.searchPlaces()
    }
  }
</script>

<style>

  .columns {
    margin: 0;
  }


  a {
    color: #454545;
  }

  #grid_places {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    grid-gap: 10px;
    justify-content: center;
    text-align: center;
  }

  #form_grid {
    margin-bottom: 15px;
  }

  @media screen and (min-width: 769px) {
      #form_grid {
        margin-bottom: 15px;
        position: sticky; 
        height: 90vh;
        top: 0;
      }
      #header_txt {
        font-size: 10px;
      }
    }

  #img_header_box {
    display: flex;
    align-items: center;
    justify-content: right;
  }

  #img_header {
    width: 400px;
    height: 400px;
  }

  #header_txt {
    font-size: 2em;
    /* max-width: 250px; */
    font-weight: bold;
    padding-left: 35px;
    padding-right: 35px;
    color: #454545;
    text-align: left;
    line-height: normal;
    /* font-family: Arial, Helvetica, sans-serif; */
  }

  #legend_header {
    font-size: 1rem;
    font-weight: normal;
    margin-top: 15px;

  }

  #header_txt_box {
    display: flex;
    align-items: center;
    justify-content: left;
  }

  #header {
    padding-bottom: 30px;
    background-color: whitesmoke;
    padding-top: 30px;

  }

  .type_scroll { 
    border:2px solid #ccc; 
    width:80%; 
    height: 25vh; 
    overflow-y: scroll; 
    color: #454545;
  }

  .scroll_items {
    text-align: left;
    padding-left: 15px;
    color: #454545;
  }

    .scroll_items label {
      padding-left: 7px;
  }

  .form_title {
    font-size: 20px;
    max-width: 250px;
    font-weight: bold;
    color: #454545;
    text-align: center;
  }

  #form {
    margin-top: 15px;
  }

  #form_right, #form_left {
    margin-bottom: 15px;

  }

.button {
  width: 80%;
}

.button_box {
    display: flex;
  justify-content: center;
}

.button:hover {
  background-color: whitesmoke;
}

body {
  color: #454545;
}

</style>