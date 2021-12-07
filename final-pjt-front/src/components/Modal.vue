<template>

<transition name="fade" appear>
  <div class="modal d-flex align-items-center justify-content-center" 
    v-if="visible" @click.self="handleWrapperClick">
    <div class="modal__dialog ">
      <header class="modal__header">
        <span>{{title}}</span>
        <div class="modal_btn">
          <button @click="$emit('update:visible', !visible)" class ="btn btn-secondary m-4">X</button>
        </div>
      </header>
      <div class="modal__body">
        <slot></slot>
      </div>
    </div>
  </div>
</transition>


</template>

<script>
export default {
  name: 'Modal',
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    title: {
      type: String,
      require: false,
    },
  },
  methods: {
    handleWrapperClick(){
      this.$emit('update:visible', false)
    },
  },
}
</script>

<style lang="scss">
$module: 'modal';
.#{$module} {
  z-index: 4000 !important;
  background-color: rgba(0, 0, 0, 0.7) !important;
  width: 1000px !important;
  vertical-align: middle !important;
  position: absolute !important;
  overflow: inherit !important;
  margin: 0 !important;

  &__dialog{    
    display: flex;
    border: 2px solid white;
    vertical-align: middle;
    position: static;
  }
  &container{
    width: 1000px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.664);
    transition: all .3s ease;
    position: static;
  }

  &_header {
    font-size: 28px;
    font-weight: bold;
    line-height: 1.29;
    padding: 16px 16px 0 25px;
    position: fixed;
  }

  &__body {
    padding: 25px;
    min-height: 150px;
    max-height: 500px;
    // overflow-y: scroll;
  }

  &_btn {
    float: left;
  }
}
</style>