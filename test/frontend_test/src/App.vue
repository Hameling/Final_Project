<template>
  <div id="app">
    <!--로그인 Modal 시작부-->
    <LoginForm v-on:sessionCheck="sessionCheck"/>
    <LogoutForm v-on:sessionCheck="sessionCheck"/>
    <RegisterForm/>
    <createTitle v-on:get-basedata="getBaseData"/>
    <!--로그인 Modal 끝 -->

    <nav class="navbar navbar-expand navbar-dark bg-dark static-top">
      <a style="color:white" class="navbar-brand mr-1">L.O.O</a>

      <!-- Navbar Search -->
      <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0">
        <div v-if="session_checked">
          <a style="color:white">환영합니다. {{returnUID()}}님</a>
        </div>
      </form>
    </nav>

    <div id="wrapper">
      <!-- Sidebar -->
      <!--세션이 있을때-->
      <ul class="sidebar navbar-nav" v-show="session_checked">
        <center>
          <li class="nav-item active">
            <div class="nav-link" @click="moveWorkspace">
              <i class="far fa-address-book" style="padding-right: 5px;"></i>
              
                <span>Personal Workspace</span>
              
            </div>
          </li>
        </center>  

        <div>
          <br>
        </div>

        <!--프로젝트 생성 및 목록 코드는 이 밑에 작성-->

        <center>
          <div class="button-title" @click="$bvModal.show('create-title')">
            <div class="eff-title"></div>
            <a style="color: white">Create Title</a>
          </div>
        </center>

        <center>
          <div class="border-title max-height inner-col">
            <TitleList v-bind:titles="titleList"/>
          </div>
          <span class="float-right">
            <i class="times-icon">&times;</i>
          </span>
        </center>

        <!--로그아웃 버튼-->
        <li class="nav-item logout-footer">
          <div class="nav-link" @click="$bvModal.show('Logout')">
            <i class="fas fa-sign-out-alt"></i>
            <!--fa-chart-area 버튼 이미지 -->
            <span>Logout</span>
          </div>
        </li>

        <!--
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
        </li>-->
      </ul>

      <!--세션이 없을때-->
      <ul class="sidebar navbar-nav" v-show="!session_checked">
        <li class="nav-item">
          <div class="nav-link" @click="$bvModal.show('Login')">
            <i class="fas fa-sign-in-alt"></i>
            <!--fa-chart-area 버튼 이미지 -->
            <span>Sign In</span>
          </div>
        </li>

        <li class="nav-item">
          <div class="nav-link" @click="$bvModal.show('Register')">
            <i class="fas fa-user-plus"></i>
            <span>Sign Up</span>
          </div>
        </li>

        <!--
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
        </li>-->
      </ul>

      <router-view/>

      <!-- Scroll to Top Button-->
      <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
      </a>
    </div>
    <footer class="sticky-footer">
      <div class="container my-auto">
        <div class="copyright text-center my-auto">
          <span>Copyright © Library Of Owl 2019</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import LoginForm from "@/components/modal/LoginForm";
import LogoutForm from "@/components/modal/LogoutForm";
import RegisterForm from "@/components/modal/RegisterForm";
import createTitle from "@/components/modal/createTitle";
import TitleList from "@/components/TitleList";
import { bus } from "@/eventbus";

export default {
  name: "app",
  data: () => ({
    session_checked: false
    //titleList : []
  }),
  methods: {
    //세션 여부 확인용 메소드
    sessionCheck(value) {
      this.session_checked = value;
    },

    //workspace 화면에 이벤트 전달
    getBaseData() {
      bus.$emit("get-basedata");
    },

    //workspace로 이동시키기 위한 메소드
    moveWorkspace() {
      this.$router.replace("/workspace");
    },
    
    //사용자 이름을 화면 상단에 표시하기 위한 메소드
    returnUID() {
      return sessionStorage.uid;
    }
  },

  computed: {
    //동적으로 변하는 TitleList - Vuex이용
    titleList: {
      get: function() {
        return this.$store.getters.getTitleList;
      },
      set: function() {}
    }
  },
  mounted() {
    if (sessionStorage.getItem("accessToken") != null) {
      this.session_checked = true;
    }
  },
  components: {
    LoginForm: LoginForm,
    LogoutForm: LogoutForm,
    RegisterForm: RegisterForm,
    TitleList: TitleList,
    createTitle: createTitle
  }
};
</script>