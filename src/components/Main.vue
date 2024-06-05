<template>
  <div class="wrapper">
    <v-expansion-panels multiple>
      <v-expansion-panel
        v-for="data, index in items"
        :key="index"
        :text="index+1"
        :title="data"
      />
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
      'Оборудование',
      'Сотрудники',
      'Помещения',
      'Отчеты',
      'Выход из системы'
      ],
    }
  }
}
</script>

<style lang="scss">

</style>