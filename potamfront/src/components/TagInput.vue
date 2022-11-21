<template>
  <div class="tag-input">
    <div v-for="(type, index) in types" :key="type" class="tag-input__tag">
      <span @click='removeTag(index)'>x</span>
      {{ type }}
    </div>
  </div>
</template>
<script>
  export default {
    props: {
        types: Array
    },
    methods: {
        removeTag (index) {
            this.$emit('clicked', index)
    }
    }
  }
</script>
<style scoped>
  .tag-input {
    width: 100%;
    border: 1px solid #eee;
    font-size: 0.9em;
    height: 50px;
    box-sizing: border-box;
    padding: 0 10px;
  }

  .tag-input__tag {
    height: 30px;
    float: left;
    margin-right: 10px;
    background-color: #eee;
    margin-top: 10px;
    line-height: 30px;
    padding: 0 5px;
    border-radius: 5px;
    color: #454545;
  }

  .tag-input__tag > span {
    cursor: pointer;
    opacity: 0.75;
  }

  .tag-input__text {
    border: none;
    outline: none;
    font-size: 0.9em;
    line-height: 50px;
    background: none;
  }
</style>