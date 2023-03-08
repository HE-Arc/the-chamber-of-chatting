<script setup></script>

<template>
  <q-header reveal elevated class="bg-grey-10 text-white" height-hint="98">
    <q-toolbar>
      <q-icon name="question_answer" size="xl"></q-icon>
      <q-toolbar-title> The Chamber of Chatting </q-toolbar-title>
    </q-toolbar>
    <q-tabs align="left">
      <q-route-tab :to="{ name: 'home' }" label="Home" />
      <q-route-tab :to="{ name: 'new-topic' }" label="New Topic" />
      <q-route-tab :to="{ name: 'about' }" label="About" />
    </q-tabs>
  </q-header>
</template>

<style scoped></style>
