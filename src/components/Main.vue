<template>
  <div class="wrapper">
    <v-expansion-panels class="mb-4" multiple>
      <v-expansion-panel
        v-for="data, index in items"
        :title="data"
        :key="index"
      > 
        <v-expansion-panel-text>
          <equipment v-if="index === widgetEnum.equipment"/>
          <employees v-if="index === widgetEnum.employees"/>
          <premises v-if="index === widgetEnum.premises"/>
          <reports v-if="index === widgetEnum.reports"/>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-btn style="width: 100%" @click="this.$emit('logout')">Выход из системы</v-btn>
  </div>
</template>

<script>
import Employees from '@/components/widgets/Employees.vue';
import Equipment from '@/components/widgets/Equipment.vue';
import Premises from '@/components/widgets/Premises.vue';
import Reports from '@/components/widgets/Reports.vue';

export default {
  data() {
    return {
      items: [ 'Оборудование', 'Сотрудники', 'Помещения', 'Отчеты' ],
      widgetEnum: { equipment: 0, employees: 1, premises: 2, reports: 3 },
    }
  },
  components: { Employees, Equipment, Premises, Reports },
}
</script>