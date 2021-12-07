<template>
  <div class="container" style="position: absolute; top: 200px; width:100%;">
    <table class="table table-bordered table-hover" v-if="communities">
      <thead class="head">
        <tr>
          <th class="text-center" style="width: 10%;">번호</th>
          <th class="text-center" style="width: 55%;">제목</th>
          <th class="text-center" style="width: 15%;">글쓴이</th>
          <th class="text-center" style="width: 20%;">등록일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(community, idx) in paginatedData" :key="idx">
          <td class="num"><span style="color: white;">{{ community.id }}</span></td>
          <td class="num" style="text-align: start;" @click="communityDetail(community)"><span style="color: white; margin-left: 30px;">{{ community.title }}</span></td>
          <td class="num"><span style="color: white;">{{ community.auth_user }}</span></td>
          <td class="num"><span style="color: white;">{{ community.created_at|MMdd }}</span></td>
        </tr>
      </tbody>
    </table>
    <div class="btn-cover" v-if="paginatedData">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">이전</button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">다음</button>
    </div>
    <button @click="toCreateCommunity" class="create-btn">글쓰기</button>
  </div>
</template>

<script>
export default {
  name: 'CommunityList',
  props: {
    communities: {
      type: Array,
      required: true
    }
  },
  data: function() {
    return {
      pageNum: 0,
      pageSize: 10,
    }
  },
  methods: {
    communityDetail(community) {
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}` }})
    },
    toCreateCommunity: function () {
      this.$router.push({ name: 'CreateCommunity' })    
    },
    nextPage() {
      this.pageNum++
    },
    prevPage() {
      this.pageNum--
    }
  },
  computed: {
    pageCount() {
      let listLeng = this.communities.length,
      listSize = this.pageSize,
      page = Math.floor(listLeng/listSize);
      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      if (this.communities.length >= 1){
        const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;
        return this.communities.slice(start, end);
      } else {
        return 0
      }
    }
  },
  filters : {  
    MMdd : function(value){ 
      if(value == '') return '';
      let js_date = new Date(value);
      let year = js_date.getFullYear();
      let month = js_date.getMonth() + 1;
      let day = js_date.getDate();
      let hours = js_date.getHours();
      let minutes = js_date.getMinutes();
      if(month < 10){
        month = '0' + month;
      }
      if(day < 10){
        day = '0' + day;
      }
      if(hours < 10){
        hours = '0' + hours;
      }
      if(minutes < 10){
        minutes = '0' + minutes;
      }
      return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;
    }
  }
}
</script>

<style scoped>
.head {
  color: white;
  letter-spacing: .1em;
  border: hidden;
}
th {
  border-right: none;
  border-left: none;
  font-size: 18px;
}
.table {
  --bs-table-bg: transparent;
  --bs-table-accent-bg: transparent;
  --bs-table-striped-color: #212529;
  --bs-table-striped-bg: rgba(0, 0, 0, 0.05);
  --bs-table-active-color: #212529;
  --bs-table-active-bg: rgba(0, 0, 0, 0.1);
  --bs-table-hover-color: #212529;
  --bs-table-hover-bg: rgba(0, 0, 0, 0.075);
  width: 100%;
  margin-bottom: 1rem;
  color: #212529;
  vertical-align: top;
  border-color: #dee2e6;  
}
.table tr td.num {
  position: relative;
  margin-left: 5px;
  border-left: none;
  border-right: none;
}
.table tr td {
  padding: 8px 5px;
  text-align: center;
  vertical-align: middle;
  font-size: 15px;
}
.table tr {
  border-bottom: 1px solid #ebebeb;
}
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
  clear: both;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
  float: center;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
.page-btn:hover {
  background-color: #345389;
  cursor: pointer;
}
button {
  background: linear-gradient(125deg,#586d6d,#4d40b6,#b13e51);
  outline: transparent;
  color: white;
  border: transparent;
  border-radius: 5px;
}

.create-btn{
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
  float:right;
  background: linear-gradient(125deg,#586d6d,#4d40b6,#b13e51);
}
</style>