import Monkey from './monkey.js';

class people extends Monkey{
    constructor(name){
        super(name);
    }

    think(){
        return `${this.name}:\"来就来，谁怕谁！\"`;
    }

    process(){
        return setTimeout(() => {
            console.log(`
            +-+-+-+-+-+-+-+
            +-+-+-+-+-+-+-+
            +-+-+-+-+-+-+-+
            +-+-+-+-+-+-+-+
            激烈打斗中...
            `);
        }, 1500);
    }

    result(){
        return setTimeout(() => {
            console.log(`
            最终${this.name}打跑了狒狒!`);
        }, 4500);
    }
}

export default people;