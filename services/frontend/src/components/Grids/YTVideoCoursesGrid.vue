<template>
  <div class="container mx-auto px-4">
    <div class="grid grid-cols-5 gap-4">
      <YTVideoCourseCard
        v-for="(course, index) in courses"
        :key="index"
        :courseThumbnail="course.thumbnail"
        :courseTitle="course.title"
        :channelName="course.channelName"
        :views="course.views"
        :uploadDate="course.uploadDate"
        :videoCount="course.videoCount"
        :courseLength="course.length"
      />
    </div>
  </div>
</template>

<script>
import YTVideoCourseCard from "@/components/Cards/YTVideoCourseCard.vue";

export default {
  name: "YTVideoCoursesGrid",
  components: {
    YTVideoCourseCard,
  },
  data() {
    return {
      courses: [
        {
          thumbnail: "https://i.ytimg.com/vi/xyVfLxV08I0/maxresdefault.jpg",
          title: "Some random video title",
          channelName: "Some channel",
          views: "351K",
          uploadDate: "3rd Oct 2021",
          videoCount: 14,
          length: "5h 37m",
        },
      ],
    };
  },
};
</script>

<style scoped></style>
