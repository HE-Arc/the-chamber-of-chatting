<!-- <template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template> -->


<template>
  <q-page padding>
    <q-btn color="primary" :to="{ name: 'home' }">
      <q-icon left name="arrow_back" />
      <div>Back</div>
    </q-btn>
      <div class="row self-center justify-evenly">
        <div class="col-12 q-mt-md">
          <q-card class="q-pa-lg">

            <q-card-section class="text-center">
              <div class="text-h5">About page</div>
            </q-card-section>

          </q-card>
        </div>
      </div>
  </q-page>
</template>

<style scoped></style>
