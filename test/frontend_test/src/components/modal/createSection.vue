<template>
  <b-modal
    id="create-section"
    title="Create Section"
    centered
    ref="modal"
    @show="resetModal"
    @hidden="resetModal"
    @ok="handleOk"
  >
    <form ref="form" @submit.stop.prevent="handleSubmit">
      <b-form-group
        :state="nameState"
        label="Section Name"
        label-for="name-input"
        invalid-feedback="Section Name is required"
      >
        <b-form-input id="name-input" v-model="sectionname" :state="nameState" required></b-form-input>
      </b-form-group>
    </form>
  </b-modal>
</template>


<script>
export default {
  name: "createSection",
  data: () => ({
    sectionname: "",
    nameState: null
  }),
  methods: {
    getSection() {
      this.$emit("get-section");
    },
    createSection() {
      if(this.doubleSubmitCheck()) return;
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://110.11.72.247:20000/section/create-section/", {
            titleid: sessionStorage.titleid,
            sectionname: this.sectionname,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getSection();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
    //Modal 관련코드
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.sectionname = "";
      this.nameState = null;
      this.doubleSubmitFlag = false;
    },
    handleOk(bvModalEvt) {
      bvModalEvt.preventDefault();
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
        this.createSection();
      });
    }
  }
};
</script>ß