import Car from './10-car.js';

export default class EVCar extends Car {
    constructor(brand,motor,color,range) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
        this._range = range;
    }

    cloneCar() {
        const clone = new (
        Object.getPrototypeOf(this.constructor))(this._brand, this._motor, this._color);
        clone._range = this._range;
        return clone;
    }
}