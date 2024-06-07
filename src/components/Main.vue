<template>
  <div class="wrapper">
    <v-expansion-panels class="mb-4" multiple>
      <v-expansion-panel
        v-for="data, index in items"
        :title="data"
        :key="index"
      > 
        <v-expansion-panel-text>
          <!-- Оборудование -->
          <div v-if="index === widgetEnum.equipment">
            <!-- Добавление оборудования -->
            <btn-with-form-dialog
              header-text="Добавление оборудования"
              btn-text="Добавить"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :addFunction="equipmentAddFunction"
              is-add
            >
              <v-text-field
                v-for="data, index in equipmentAddDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- Редактирование оборудования -->
            <btn-with-form-dialog
              header-text="Редактирование оборудования"
              btn-text="Редактировать"
              :max-width="1200"
              :is-access-action="isAccessAction"
              :is-error-action="isErrorAction"
              :editFunction="equpmentEditFunction"
              is-edit
            >
              <v-text-field
                v-for="data, index in equipmentEditDialogInputItems" :key="index"
                v-model="data.dataModel"
                :label="data.labelText"
              />
            </btn-with-form-dialog>
            <!-- <v-btn @click="openDialog('EquipmentEditDialog')" class="mr-1 mb-2"> Редактировать </v-btn> -->
            <v-btn @click="openDialog('EquipmentDeleteDialog')" class="mr-1 mb-2"> Списать </v-btn>
            <!-- Посмотреть записи оборудования -->
            <btn-with-list-dialog
              header-text="Список оборудования"
              btn-text="Посмотреть записи"
              :max-width="700"
              :headers="EquipmentListDialogHeaders"
              :items="equipmentListDialogItems"
            />
          </div>
          <div v-if="index === widgetEnum.employees">
            <v-btn @click="openDialog('EmployeesAddDialog')" class="mr-1 mb-2"> Добавить МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesEditDialog')" class="mr-1 mb-2"> Редактировать МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesDeleteDialog')" class="mr-1 mb-2"> Уволить МОЛ </v-btn>
            <v-btn @click="openDialog('EmployeesTrustedEquipmentDialog')" class="mr-1 mb-2"> Доверенное оборудование </v-btn>
            <!-- Посмотреть записи МОЛов -->
            <btn-with-list-dialog
              header-text="Список МОЛов"
              btn-text="Посмотреть записи"
              :max-width="1200"
              :headers="EmployeesListDialogHeaders"
              :items="EmployeesListDialogItems"
            />
          </div>
          <div v-if="index === widgetEnum.premises">
            <!-- Посмотреть записи помещений -->
            <btn-with-list-dialog
              header-text="Список помещений"
              btn-text="Посмотреть записи"
              :max-width="650"
              :headers="PremisesListDialogHeader"
              :items="PremisesListDialogItems"
            />
          </div>
          <div v-if="index === widgetEnum.reports">
            <btn-with-form-dialog
              header-text="Отчетов нет"
              btn-text="Посмотреть отчеты"
              :max-width="300"
            />
          </div>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-btn style="width: 100%" @click="this.$emit('logout')">Выход из системы</v-btn>
  </div>
</template>

<script>
import BtnWithListDialog from '@/components/widgets/BtnWithListDialog.vue';
import BtnWithFormDialog from '@/components/widgets/BtnWithFormDialog.vue';

export default {
  components: { BtnWithListDialog, BtnWithFormDialog },
  data() {
    return {
      items: [ 'Оборудование', 'Сотрудники', 'Помещения', 'Отчеты' ],
      widgetEnum: { equipment: 0, employees: 1, premises: 2, reports: 3 },
      equipmentAddDialogInputItems: [
        { dataModel: '', labelText: 'Код оборудования' },
        { dataModel: '', labelText: 'Инвентарный номер' },
        { dataModel: '', labelText: 'Состояние' },
        { dataModel: '', labelText: 'Код типа оборудования' },
      ],
      equipmentEditDialogInputItems: [
        { dataModel: '', labelText: 'id *'},
        { dataModel: '', labelText: 'Код оборудования' },
        { dataModel: '', labelText: 'Инвентарный номер' },
        { dataModel: '', labelText: 'Состояние' },
        { dataModel: '', labelText: 'Код типа оборудования' },
      ],
      equipmentListDialogItems: [
        { id: 1, inventoryCode: 505, inventoryNumber: 100501, state: 'Active', typeCodeEquipment: 600},
        { id: 2, inventoryCode: 555, inventoryNumber: 100502, state: 'Active', typeCodeEquipment: 450},
        { id: 3, inventoryCode: 565, inventoryNumber: 100503, state: 'Disabled', typeCodeEquipment: 450},
        { id: 4, inventoryCode: 575, inventoryNumber: 100504, state: 'Active', typeCodeEquipment: 600},
        { id: 5, inventoryCode: 585, inventoryNumber: 100505, state: 'Active', typeCodeEquipment: 550},
      ],
      isAccessAction: false,
      isErrorAction: false,
    }
  },
  methods: {
    equipmentAddFunction() {
      if(!this.equipmentAddDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      this.equipmentListDialogItems.push({
        id: this.equipmentListDialogItems.length+1,
        inventoryCode: this.equipmentAddDialogInputItems[0].dataModel,
        inventoryNumber: this.equipmentAddDialogInputItems[1].dataModel,
        state: this.equipmentAddDialogInputItems[2].dataModel,
        typeCodeEquipment: this.equipmentAddDialogInputItems[3].dataModel
      });
      this.equipmentAddDialogInputItems = this.equipmentAddDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    },
    equpmentEditFunction() {
      if(!this.equipmentEditDialogInputItems.every(item => item.dataModel)) return this.isErrorAction = true;
      this.isAccessAction = true;
      const id = this.equipmentEditDialogInputItems[0].dataModel;
      const index = this.equipmentListDialogItems.findIndex(el => el.id == id);
      this.equipmentListDialogItems.splice(index, 1);
      this.equipmentListDialogItems.splice(index, 0, {
        id: id,
        inventoryCode: this.equipmentEditDialogInputItems[1].dataModel,
        inventoryNumber: this.equipmentEditDialogInputItems[2].dataModel,
        state: this.equipmentEditDialogInputItems[3].dataModel,
        typeCodeEquipment: this.equipmentEditDialogInputItems[4].dataModel
      });
      this.equipmentAddDialogInputItems = this.equipmentAddDialogInputItems.map(item => { return { dataModel: '', labelText: item.labelText }});
    }
  },
  computed: {
    EquipmentListDialogHeaders() {
      return [
        { title: 'id', align: 'start', key: 'id'},
        { title: 'Код оборудования', align: 'start', key: 'inventoryCode' },
        { title: 'Инвентарный номер', align: 'end', key: 'inventoryNumber' },
        { title: 'Состояние', align: 'end', key: 'state' },
        { title: 'Код типа оборудования', align: 'end', key: 'typeCodeEquipment' },
      ]; 
    },
    EmployeesListDialogHeaders() {
      return [
        { title: 'id', align: 'start', key: 'id'},
        { title: 'Код сотрудника', align: 'start', key: 'codeEmployee'},
        { title: 'Фамилия', align: 'center', key: 'surnameEmployee'},
        { title: 'Имя', align: 'center', key: 'firstnameEmployee'},
        { title: 'Отчество', align: 'center', key: 'lastnameEmployee'},
        { title: 'Телефон', align: 'center', key: 'telephoneEmployee'},
        { title: 'Код должности', align: 'center', key: 'jobCodeEmployee'},
        { title: 'Код подразделения', align: 'center', key: 'departmentCodeEmployee'},
        { title: 'Электронная почта', align: 'center', key: 'emailEmployee'},
      ];
    },
    EmployeesListDialogItems() {
      return [
        { id: 1, codeEmployee: 1, surnameEmployee: 'Третьяков', firstnameEmployee: 'Никита', 
          lastnameEmployee: 'Валерьевич', telephoneEmployee: '79992503327', jobCodeEmployee: '120', 
          departmentCodeEmployee: '320' , emailEmployee: 'fentomi02@mail.ru'
        },
        { id: 2, codeEmployee: 2, surnameEmployee: 'Спарк', firstnameEmployee: 'Алексей', 
          lastnameEmployee: 'Валентинович', telephoneEmployee: '7900345876', jobCodeEmployee: '119', 
          departmentCodeEmployee: '320' , emailEmployee: 'alexeySparking@mail.ru'
        },
        { id: 3, codeEmployee: 1, surnameEmployee: 'Третьяков', firstnameEmployee: 'Никита', 
          lastnameEmployee: 'Валерьевич', telephoneEmployee: '79992503327', jobCodeEmployee: '120', 
          departmentCodeEmployee: '320' , emailEmployee: 'fentomi02@mail.ru'
        },
        { id: 4, codeEmployee: 2, surnameEmployee: 'Спарк', firstnameEmployee: 'Алексей', 
          lastnameEmployee: 'Валентинович', telephoneEmployee: '7900345876', jobCodeEmployee: '119', 
          departmentCodeEmployee: '320' , emailEmployee: 'alexeySparking@mail.ru'
        },
        { id: 5, codeEmployee: 1, surnameEmployee: 'Третьяков', firstnameEmployee: 'Никита', 
          lastnameEmployee: 'Валерьевич', telephoneEmployee: '79992503327', jobCodeEmployee: '120', 
          departmentCodeEmployee: '320' , emailEmployee: 'fentomi02@mail.ru'
        },
        { id: 6, codeEmployee: 2, surnameEmployee: 'Спарк', firstnameEmployee: 'Алексей', 
          lastnameEmployee: 'Валентинович', telephoneEmployee: '7900345876', jobCodeEmployee: '119', 
          departmentCodeEmployee: '320' , emailEmployee: 'alexeySparking@mail.ru'
        },
      ]
    },
    PremisesListDialogHeader() {
      return [
        { title: 'id', align: 'start', key: 'id'},
        { title: 'Код помещения', align: 'start', key: 'roomСode'},
        { title: 'Название помещения', align: 'center', key: 'roomName'},
        { title: 'Номер помещения', align: 'center', key: 'roomNumber'},
        { title: 'Код подразделения', align: 'center', key: 'departmentCode'},
      ];
    },
    PremisesListDialogItems() {
      return [
        { id: 1, roomСode: 100, roomName: 'Столовая', roomNumber: 100500, departmentCode: 320},
        { id: 2, roomСode: 101, roomName: 'Гостинная', roomNumber: 100501, departmentCode: 320},
        { id: 3, roomСode: 102, roomName: 'Диванная', roomNumber: 100502, departmentCode: 320},
        { id: 4, roomСode: 103, roomName: 'Стуловая', roomNumber: 100503, departmentCode: 420},
        { id: 5, roomСode: 104, roomName: 'Коверная', roomNumber: 100504, departmentCode: 420},
      ]
    },
  },
}
</script>