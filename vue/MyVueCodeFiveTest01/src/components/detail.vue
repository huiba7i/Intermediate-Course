<template>
  <div>
    <div class="row row-title row-margin">
      <div class="col-xs-12 col-sm-6 col-md-3">
        <img :src="changePath" alt="phone" class="pictureSize">
      </div>
      <div class="col-xs-12 col-sm-6 col-md-9 cellPhoneNname">
        <h2>{{ phoneDet.name }}</h2>
        <hr>
        <p class="lead">{{ phoneDet.description }}</p>

        <div class="row">
          <div
            class="col-xs-6 col-sm-4 col-md-2"
            v-for="phoneImg in phoneDet.images"
            :key="phoneImg.id"
          >
            <a href="javascript:void(0);" class="thumbnail phonePricue">
              <img :src="phoneImg" :alt="phoneImg" @mouseover="path">
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="row list-item row-margin">
      <div class="col-xs-6 col-sm-3 col-md-1 col-md-offset-1">
        <b>Availability and Networks Availability</b>
        <p v-for="availability in phoneDet.availability" :key="availability">{{availability}}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.battery">
        <b>Battery</b>
        <br>
        <b>Type</b>
        <p>{{ phoneDet.battery.type }}</p>
        <b>Talk Time</b>
        <p>{{ phoneDet.battery.talkTime }}</p>
        <b>Standby time(max)</b>
        <p >{{ phoneDet.battery.standbyTime }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1"  v-if="phoneDet.storage">
        <b>Storage and Memory RAM</b>
        <p>{{ phoneDet.storage.ram }}</p>
        <b>Internal Storage</b>
        <p>{{ phoneDet.storage.flash }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.connectivity">
        <b>Connectivity Networks Support</b>
        <p>{{ phoneDet.connectivity.cell }}</p>
        <b>WiFi</b>
        <p>{{ phoneDet.connectivity.wifi }}</p>
        <b>Bluetooth</b>
        <p>{{ phoneDet.connectivity.bluetooth }}</p>
        <b>Infrared</b>
        <p>{{ (phoneDet.connectivity.infrared==true?'√':'×') }}</p>
        <b>GPS</b>
        <p>{{ (phoneDet.connectivity.gps==true?'√':'×') }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.android">
        <b>Android OS Version</b>
        <p>{{ phoneDet.android.os }}</p>
        <b>UI</b>
        <p>{{ phoneDet.android.ui }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.sizeAndWeight">
        <b>Size and Weight Dimensions</b>
        <p
          v-for="dimensions in phoneDet.sizeAndWeight.dimensions"
          :key="dimensions"
        >{{ dimensions }}</p>
        <b>Weight</b>
        <p>{{ phoneDet.sizeAndWeight.weight }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.display">
        <b>Display</b>
        <br>
        <b>Screen size</b>
        <p>{{ phoneDet.display.screenSize }}</p>
        <b>Screen resolution</b>
        <p>{{ phoneDet.display.screenResolution }}</p>
        <b>Touch screen</b>
        <p>{{ (phoneDet.display.touchScreen?'√':'×') }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.hardware">
        <b>Hardware</b>
        <br>
        <b>CPU</b>
        <p>{{ phoneDet.hardware.cpu }}</p>
        <b>USB</b>
        <p>{{ phoneDet.hardware.usb }}</p>
        <b>Audio/headphone jack</b>
        <p>{{ phoneDet.hardware.audioJack }}</p>
        <b>FM Radio</b>
        <p>{{ (phoneDet.hardware.fmRadio?'√':'×') }}</p>
        <b>Accelerometer</b>
        <p>{{ (phoneDet.hardware.accelerometer?'√':'×') }}</p>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1" v-if="phoneDet.camera">
        <b>Camera</b>
        <br>
        <b>Primary</b>
        <p>{{ phoneDet.camera.primary }}</p>
        <b>Features</b>
        <span v-for="features in phoneDet.camera.features" :key="features">{{ features }},</span>
      </div>
      <div class="col-xs-6 col-sm-3 col-md-1">
        <b>Additional Features</b>
        <p>{{ phoneDet.additionalFeatures }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      phoneDet: {},
      changePath: ""
    };
  },
  methods: {
    path() {
      this.changePath = event.target.alt;
    },
    getData() {
      this.$axios
        .get(`/static/phones/${this.$route.params.id}.json`)
        .then(resp => {
          this.phoneDet = resp.data;
          this.changePath = this.phoneDet.images[0];
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getData();
  }
};
</script>

<style scoped>
.pictureSize {
  width: 100%;
  height: 100%;
}
.row-margin {
  margin: 0;
}
.list-item {
  margin-top: 30px;
}
</style>

