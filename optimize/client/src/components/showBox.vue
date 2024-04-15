<template>
    <hr color="mediumorchid">
    <div class="row">
        <div class="col-5">
            <p style="padding-top: 25%;"><strong>Оптимальные значения по методу Бокса:</strong></p>
            <p><span style="font-weight: bold;">Т<sub>1</sub> = </span> {{ resultBox[0] }}&#176;С</p>
            <p><span style="font-weight: bold;">Т<sub>2</sub> = </span> {{ resultBox[1] }}&#176;С</p>
            <p><span style="font-weight: bold;">С = </span> {{ resultBox[2] }} кг за 8 часов</p>
            <p><span style="font-weight: bold;">Время расчета = </span> {{ resultBox[3] }} мкс</p>
        </div>
        <div class="col-7">
          <p class="img">
            <img src= "../../../server/Box.png">
          </p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Box',
  data() {
    return {
      resultBox: [],
    };
  },
  methods: {
    getBox() {
      const path = 'http://localhost:5001/Box';
      axios.get(path)
        .then((res) => {
          this.resultBox = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getBox();
  },
};
</script>