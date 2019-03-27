import student from './student.js';

export default class graduate extends student{
    constructor(id, name, gender, birthday, subject, adviser){
        super(id, name, gender, birthday);
        this.subject = subject;
        this.adviser = adviser;
    }

    displayTwo(){
        return console.log(`id:${this.id},name:${this.name},gender:${this.gender},birthday:${this.birthday},subject:${this.subject},adviser:${this.adviser}`);
    }
}