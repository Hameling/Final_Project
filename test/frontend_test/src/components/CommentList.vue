<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <!-- 내가 쓴 코멘트 일때 -->
      <li v-if="comment.memberid == memberid" class="my-comment-border" v-bind:id="'mycomment'+i">
        {{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime)}}]
        <!-- popover 시작부분 -->
        <b-popover v-bind:target="'mycomment'+i" v-bind:ref="'popover'+i">
          <div>
            <p>Comment를 삭제하시겠습니까?</p>
            <div class="wrap">
              <b-button class="comment-delbtn-ok" variant="primary" v-on:click="delComment(comment.comnumber, i)">Ok</b-button>
              <b-button class="comment-delbtn-no" variant="danger" v-on:click="closePop(i)">Cancel</b-button>
            </div>
          </div>
        </b-popover>
      </li>
      <!-- 다른 사람이 쓴 코멘트 일때 -->
      <li
        v-else
        class="other-comment-border"
      >{{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime)}}]</li>
      
    </ul>
  </div>
</template> 

<script>
export default {
  name: "CommentList",
  props: ["comments"],
  data: () => ({
    memberid: sessionStorage.uid,

  }),
  methods: {
    delComment(comment, index) {
      this.$emit("del-comment", comment);
      this.closePop(index)
    },
    closePop(index){
        this.$refs["popover" + index][0].$emit('close')
    },

    formattingTime(time) {
      var tmp = time.substring(0, time.length - 3);
      return tmp;
    },
  },

};
</script>