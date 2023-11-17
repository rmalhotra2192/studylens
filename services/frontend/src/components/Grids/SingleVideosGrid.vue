<template>
  <div class="container mx-auto px-4">
    <div class="grid grid-cols-5 gap-4">
      <SingleVideoCard
        v-for="(video, index) in videos"
        :key="index"
        :videoThumbnail="video.thumbnail"
        :videoTitle="video.title"
        :channelName="video.channelName"
        :views="video.views"
        :uploadDate="video.uploadDate"
      />
    </div>
  </div>
</template>

<script>
import SingleVideoCard from "@/components/Cards/SingleVideoCard.vue";

export default {
  name: "SingleVideosGrid",
  components: {
    SingleVideoCard,
  },
  data() {
    return {
      videos: [
        {
          thumbnail: "https://i.ytimg.com/vi/xyVfLxV08I0/maxresdefault.jpg",
          title: "Some random video title",
          channelName: "Some channel",
          views: "351K",
          uploadDate: "3rd Oct 2021",
        },
      ],
    };
  },
};
</script>

<style scoped></style>
