export default class student{
    constructor(id, name, gender, birthday){
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.birthday = birthday;
    }

    display(){
        return console.log(`id:${this.id},name:${this.name},gender:${this.gender},birthday:${this.birthday}`);
    }
}