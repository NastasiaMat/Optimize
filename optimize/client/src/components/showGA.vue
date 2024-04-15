<template>
    <hr color="mediumorchid">
    <div class="row">
        <div class="col-5">
            <p style="padding-top: 25%;"><strong>Оптимальный температурный режим по ГА:</strong></p>
            <p><span style="font-weight: bold;">Т<sub>1</sub> = </span> {{ resultGA[0] }}&#176;С</p>
            <p><span style="font-weight: bold;">Т<sub>2</sub> = </span> {{ resultGA[1] }}&#176;С</p>
            <p><span style="font-weight: bold;">С = </span> {{ resultGA[2] }} кг за 8 часов</p>
            <p><span style="font-weight: bold;">Время расчета = </span> {{ resultGA[3] }} мкс</p>
        </div>
        <div class="col-7">
          <p class="img">
            <img src= "../../../server/GA.png">
          </p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GA',
  data() {
    return {
      resultGA: [],
    };
  },
  methods: {
    getGA() {
      const path = 'http://localhost:5001/GA';
      axios.get(path)
        .then((res) => {
          this.resultGA = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getGA();
  }
};
</script>