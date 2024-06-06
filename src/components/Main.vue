<template>
  <div class="wrapper">
    <v-expansion-panels class="mb-4" multiple>
      <v-expansion-panel
        v-for="data, index in items"
        :title="data"
        :key="index"
      > 
        <v-expansion-panel-text>
          <div v-if="index === widgetEnum.equipment">
            <v-btn @click="openDialog('EquipmentAddDialog')" class="mr-1 mb-2"> Добавить </v-btn>
            <v-btn @click="openDialog('EquipmentEditDialog')" class="mr-1 mb-2"> Редактировать </v-btn>
            <v-btn @click="openDialog('EquipmentDeleteDialog')" class="mr-1 mb-2"> Списать </v-btn>
            <v-btn @click="openDialog('EquipmentListDialog')" class="mr-1 mb-2"> Посмотреть записи </v-btn>
          </div>
          <div v-if="index === widgetEnum.employees">
            <v-btn @click="openDialog('EmployeesAddDialog')" class="mr-1 mb-2"> Добавить МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesEditDialog')" class="mr-1 mb-2"> Редактировать МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesDeleteDialog')" class="mr-1 mb-2"> Уволить МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesTrustedEquipmentDialog')" class="mr-1 mb-2"> Доверенное оборудование </v-btn>
            <v-btn @click="openDialog('EmployeesListDialog')" class="mr-1 mb-2"> Посмотреть записи </v-btn>
          </div>
          <div v-if="index === widgetEnum.premises">
            <v-btn @click="openDialog('PremisesListDialog')" class="mr-1 mb-2"> Посмотреть записи </v-btn>
          </div>
          <div v-if="index === widgetEnum.reports">
            <v-btn @click="openDialog('ReportsListDialog')" class="mr-1 mb-2"> Принять отчет </v-btn>
          </div>
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
  methods: {
    openDialog(typeDialog) {
      switch (typeDialog) {
        case 'EquipmentAddDialog': console.log('1'); break;
        case 'EquipmentEditDialog': console.log('2'); break;
        case 'EquipmentDeleteDialog': console.log('3'); break;
        case 'EquipmentListDialog': console.log('4'); break;
        case 'EmployeesAddDialog': console.log('5'); break;
        case 'EmployeesEditDialog': console.log('6'); break;
        case 'EmployeesDeleteDialog': console.log('7'); break;
        case 'EmployeesTrustedEquipmentDialog': console.log('8'); break;
        case 'EmployeesListDialog': console.log('9'); break;
        case 'PremisesListDialog': console.log('10'); break;
        case 'ReportsListDialog': console.log('11'); break;
      }
    }
  }
}
</script>