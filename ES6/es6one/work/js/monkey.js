class Monkey{
    constructor(name){
        this.name = name;
    }

    speak(){
        return `${this.name}:\"小样，来互相伤害呀！\"`;
    }

    fullName(){
        return this.name;
    }
}
export default Monkey;