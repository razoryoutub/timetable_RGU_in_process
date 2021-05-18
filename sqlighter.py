import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_users(self):
        """Получаем всех пользователей бота"""
        with self.connection:
            return self.cursor.execute("SELECT `ID`, `user-id`, `user-first-name`, `user-last-name`, `username` FROM `users`").fetchall()

    def user_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT `ID` FROM `users` WHERE `user-id` = ?', (user_id, )).fetchall()
            if (result == []):
                return False
            else:
                return True


    def add_user(self, message):
        """Добавляем нового пользователя"""
        with self.connection:
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name
            user_last_name = message.from_user.last_name
            username = message.from_user.username
            self.cursor.execute("INSERT INTO `users` (`user-id`, `user-first-name`, `user-last-name`, `username`) VALUES(?,?,?,?)", (user_id, user_first_name, user_last_name, username))


    def comand_statistic(self, comand_name):
        with self.connection:
            value = (self.cursor.execute('SELECT `comand-value` from `comands` WHERE `comand-name` = ?',(comand_name, )).fetchall())[0][0]
            value+=1
            self.cursor.execute("UPDATE `comands` SET `comand-value` = ? WHERE `comand-name` = ?",(value, comand_name)).fetchall()


    def get_comand_statistic(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `comands`").fetchall()


    def user_used(self, user):
        with self.connection:
            value = (self.cursor.execute('SELECT `count-used` from `users` WHERE `user-id` = ?',(user, )).fetchall())[0][0]
            value+=1
            self.cursor.execute("UPDATE `users` SET `count-used` = ? WHERE `user-id` = ?",(value, user)).fetchall()


    def save_week(self,user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_week` = ? WHERE `user-id` = ?",(True, user_id)).fetchall()


    def remove_week(self,user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_week` = ? WHERE `user-id` = ?",(False, user_id)).fetchall()


    def save_fack(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_fack` = ? WHERE `user-id` = ?",(True, user_id)).fetchall()


    def remove_fack(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_fack` = ? WHERE `user-id` = ?",(False, user_id)).fetchall()

    def save_group(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_group` = ? WHERE `user-id` = ?",(True, user_id)).fetchall()

    def remove_group(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `save_group` = ? WHERE `user-id` = ?",(False, user_id)).fetchall()


    def get_settings_status(self, user_id):
        with self.connection:
            week = self.cursor.execute("SELECT `save_week` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            fack = self.cursor.execute("SELECT `save_fack` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            group = self.cursor.execute("SELECT `save_group` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            return(week,fack,group)


    def get_settings(self, user_id):
        with self.connection:
            week = self.cursor.execute("SELECT `saved_week` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            fack = self.cursor.execute("SELECT `saved_fack` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            group = self.cursor.execute("SELECT `saved_group` FROM `users` WHERE `user-id` = ?",(user_id,)).fetchall()
            return(week,fack,group)


    def add_week(self,user_id,week):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_week` = ? WHERE `user-id` = ?",(week, user_id)).fetchall()


    def clear_week(self,user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_week` = ? WHERE `user-id` = ?",(None, user_id)).fetchall()


    def add_fack(self, user_id,fack):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_fack` = ? WHERE `user-id` = ?",(fack, user_id)).fetchall()


    def clear_fack(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_fack` = ? WHERE `user-id` = ?",(None, user_id)).fetchall()

    def add_group(self, user_id,group):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_group` = ? WHERE `user-id` = ?",(group, user_id)).fetchall()

    def clear_group(self, user_id):
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `saved_group` = ? WHERE `user-id` = ?",(None, user_id)).fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()