<template>
  <div class="container">
    <div class="row" style="padding-top: 16px">
      <div class="col-sm-12">
        <h2 style= "color: brown">Оптимизация</h2>
        <hr color="mediumorchid">
      </div>
    </div>

    <div class="row" style="margin-bottom: 0px">
      <div class="col-sm-12">
        <p style="margin-bottom: 8px">
          Целевая функция: <strong>F(T<sub>1</sub>, T<sub>2</sub>) = С ∙ t = 
          (α ∙ (T<sub>2</sub> - T<sub>1</sub>)<sup>A<sub>1</sub></sup> + β ∙ 1/V<sub>1</sub> ∙ 
          (T<sub>1</sub> + T<sub>2</sub> - γ ∙ V<sub>2</sub>)<sup>A<sub>2</sub></sup>) ∙ t</strong>
        </p>
        <p style="margin-bottom: 2px">F(T<sub>1</sub>, T<sub>2</sub>) &#10230; <em>max</em>,</p>
        <p style="margin-bottom: 2px">при T<sub>1</sub>, T<sub>2</sub> &#8712; [-3, 14],</p>
        <p style="margin-bottom: 22px">T<sub>1</sub> + T<sub>2</sub> &#8804; 12&#176;С</p>
      </div>
    </div>

    <div class="row" style="margin-bottom: 16px">
      <div class="col-sm-4">
        <button type="button" class="btn btn-outline-danger" v-on:click="componentName = 'GA'">
          Генетический алгоритм
        </button>
      </div>
      <div class="col-sm-4">
        <button type="button" class="btn btn-outline-danger" v-on:click="componentName = 'All'">
          Сравнить
        </button>
      </div>
      <div class="col-sm-4">
        <button type="button" class="btn btn-outline-danger" v-on:click="componentName = 'Box'">
          Метод Бокса
        </button>
      </div>
    </div>
    <component :is="componentName"></component>
  </div>
</template>

<script>
import GA from './components/showGA.vue'
import Box from './components/showBox.vue'
import All from './components/showAll.vue'

export default {
  components: {
		GA,
    Box,
    All
	},
  data(){
    return {
      componentName: '',
    }
  }
};
</script>

<style>
.container {
  margin-top: 20px;
  border: 2px solid mediumorchid;
  text-align: center;
  border-radius: 20px;
  background: lavender;
}
.row {
  padding-top: 0px;
  padding-bottom: 0px;
  text-align: center;
}
.img {
  position: relative;
  height:500px;
}
.img img {
  position: absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  width:700px;
  height:500px;
  object-fit:cover;
  border: 1px solid mediumorchid;
  border-radius: 20px;
}
</style>
