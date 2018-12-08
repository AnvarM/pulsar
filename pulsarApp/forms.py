from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NoneOf
from wtforms.fields.html5 import DateField

class PulsarFeedbackForm(FlaskForm):
    block = 'blocked'
    select_message = 'Выберите нужное'
    checklist = [('blocked', '--Выбрать--'),('Опасно', 'Опасно'), ('Безопасно', 'Безопасно'), ('Не применимо', 'Не применимо')]
    department_data = [('blocked', '--Выбрать--'),('Directorate','Directorate'), ('EHS', 'EHS'), ('Engineering electric.', 'Engineering electric.'), ('Engineering mech.', 'Engineering mech.'),
                  ('FG Warehouse', 'FG Warehouse'),('Finance', 'Finance'),('HR,IT,LEX', 'HR,IT,LEX'), ('Leaf  Warehouses', 'Leaf  Warehouses'), ('LS#1', 'LS#1'),
                  ('LS#2', 'LS#2'), ('LS#3', 'LS#3'),('LS#4', 'LS#4'), ('Medical centre', 'Medical centre'), ('ODS', 'ODS'), ('PMD', 'PMD'),('PMD CTS', 'PMD CTS'),
                  ('Q & PA', 'Q & PA'), ('RRS', 'RRS'), ('Security', 'Security'), ('SMD office', 'SMD office'), ('Supply Chain (office)', 'Supply Chain (office)')]
    area_data = [('blocked', '--Выбрать--'),('4 Линия', '4 Линия'), ('5 Линия', '5 Линия'), ('7 Линия', '7 Линия'), ('8 Линия', '8 Линия'), ('9 Линия', '9 Линия'), ('10 Линия', '10 Линия'), ('17 Линия','17 Линия'),
            ('18 Линия', '18 Линия'), ('19 Линия', '19 Линия'),('31 Линия', '31 Линия'), ('51 Линия', '51 Линия'), ('52 Линия', '52 Линия'), ('53 Линия', '53 Линия'),
            ('54 Линия','54 Линия'), ('55 Линия', '55 Линия'), ('CLD-линия Берлея', 'CLD-линия Берлея'),('CTS-склад резанного табака', 'CTS-склад резанного табака'),
            ('Cutter Lamina-резка табака', 'Cutter Lamina-резка табака'), ('Cutter stem-резка черешка', 'Cutter stem-резка черешка'), ('DCCC', 'DCCC'),
            ('DRF PMD-пылесборник ПМД', 'DRF PMD-пылесборник ПМД'), ('DRF SMD-пылесборник СМД', 'DRF SMD-пылесборник СМД'),
            ('Ripper-бракобойка (находится в СМД)', 'Ripper-бракобойка (находится в СМД)'),('Slicer-загрузка табака перед DCCC', 'Slicer-загрузка табака перед DCCC'),
            ('Аналитическая', 'Аналитическая'), ('Весовая (проходная СБ)', 'Весовая (проходная СБ)'), ('Демта', 'Демта'), ('Загрузка добавок', 'Загрузка добавок'),
            ('Загрузка черешка', 'Загрузка черешка'), ('Калибраторская', 'Калибраторская'), ('Компрессорная', 'Компрессорная'), ('Контейнерная площадка', 'Контейнерная площадка'),
            ('Котельная', 'Котельная'), ('Кухня', 'Кухня'),('Линия Fibex', 'Линия Fibex'), ('Линия ориентальная', 'Линия ориентальная'),
            ('Механическая комната СМД', 'Механическая комната СМД'), ('Наружняя проходная СБ', 'Наружняя проходная СБ'), ('Офисное помещение 1 этаж' ,'Офисное помещение 1 этаж'),
            ('Офисное помещение 2 этаж', 'Офисное помещение 2 этаж'), ('Офисное помещение ПМД', 'Офисное помещение ПМД'), ('Офисное помещение СМД', 'Офисное помещение СМД'),
            ('Очистные сооружения', 'Очистные сооружения'), ('Площадка для отходов (метал, деревянная и пластиковая)', 'Площадка для отходов (метал, деревянная и пластиковая)'),
            ('Помещение Водоподготовки', 'Помещение Водоподготовки'), ('Разгрузка черешка в короба', 'Разгрузка черешка в короба'), ('Сады', 'Сады'),
            ('Сварочный участок', 'Сварочный участок'), ('Склад RRS', 'Склад RRS'), ('Склад WMS', 'Склад WMS'), ('Склад ГП', 'Склад ГП'),('Склад ОДС', 'Склад ОДС'),
            ('Склад табака №1', 'Склад табака №1'), ('Склад табака №2', 'Склад табака №2'), ('Склад табака №3', 'Склад табака №3'), ('Станочный цех' ,'Станочный цех'),
            ('Уборка помещений (укажите цех или отдел)', 'Уборка помещений (укажите цех или отдел)'), ('Уборка территории снаружи', 'Уборка территории снаружи'),
            ('Участок подготовка кейсинга/табаков', 'Участок подготовка кейсинга/табаков'), ('Физическая', 'Физическая'), ('Химическая', 'Химическая'),
            ('Чистка оборудования (укажите цех или офис)', 'Чистка оборудования (укажите цех или офис)'), ('Электрическая комната СМД', 'Электрическая комната СМД' )]
    activity_data = [('blocked', '--Выбрать--'),('Производство(обычная работа)', 'Производство(обычная работа)'), ('Техобслуживание', 'Техобслуживание'), ('Транспортировка', 'Транспортировка'),
                ('Загрузка', 'Загрузка'), ('Выгрузка', 'Выгрузка'), ('Чистка', 'Чистка'),('Работа на высоте', 'Работа на высоте')]
    shift_data = [('blocked', '--Выбрать--'),('Дневная','Дневная'), ('Ночная','Ночная'), ('Офис','Офис')]
    employee_exam_data = [('blocked', '--Выбрать--'),('Сотрудник УЗБАТ', 'Сотрудник УЗБАТ'), ('Контрактная организация', 'Контрактная организация')]
    date = DateField('Дата', validators=[DataRequired(message='Введите дату в формате ММ/ДД/ГГГГ')])
    oneviewid = StringField('Oneviewid', validators=[DataRequired(message="Введите свой oneviewid"), Length(min=8,max=8,message='Oneviewid должен быть в формате: 98909713')])
    shift = SelectField('Смена', choices=shift_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    department = SelectField('Отдел', choices=department_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    area = SelectField('Участок', choices=area_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    employee_exam = SelectField('Наблюдаемый сотрудник', choices=employee_exam_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    activity = SelectField('Обозреваемая активность', choices=activity_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    attention_work = SelectField('Внимание на работе', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    attention_road = SelectField('Внимание на дороге', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    appropriate_tools = SelectField('Использование правильных инструментов', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    tools_is_ok = SelectField('Используемые инструменты в исправности', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    ppe = SelectField('Использование необходимых СИЗ', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    ppe_special = SelectField('Использование необходимых СИЗ для спецработ', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    capture = SelectField('Избегать захвата частей тела', choices=checklist, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    comments = TextAreaField('Комментарии')
    submit = SubmitField('Отправить')


class GetUserByIdForm(FlaskForm):
    oneviewid = StringField('Oneviewid', validators=[DataRequired(message="Введите oneviewid"),Length(min=8, max=8, message='Oneviewid должен быть в формате: 98909713')])
    submit = SubmitField('Поиск')


class AddUserForm(FlaskForm):
    block = 'blocked'
    select_message = 'Выберите отдел'
    department_data = [('blocked', '--Выбрать--'),('Transport department','Transport department'), ('Cigarette workshop','Cigarette workshop'),('Engineering department','Engineering department'),
                       ('Supply Chain department','Supply Chain department'), ('Quality & Product Assurance','Quality & Product Assurance'),
                       ('Tobacco workshop','Tobacco workshop'), ('Directorate','Directorate'), ('Ecology Health and Safety','Ecology Health and Safety'),
                       ('Security','Security'), ('Finance','Finance'), ('Procurement','Procurement'), ('Medical centre','Medical centre'), ('Information Technology','Information Technology'),
                       ('Technical training','Technical training'), ('Human Resourсes','Human Resourсes'),('Legal & External Affairs Department','Legal & External Affairs Department')]
    name = StringField('Имя', validators=[DataRequired(message="Введите имя пользователя")])
    department = SelectField('Отдел', choices=department_data, validators=[DataRequired(), NoneOf(block, message=select_message)], default='blocked')
    oneviewid = StringField('Oneviewid', validators=[DataRequired(message="Введите oneviewid"), Length(min=8,max=8,message='Oneviewid должен быть в формате: 98909713')])
    submit = SubmitField('Отправить')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')