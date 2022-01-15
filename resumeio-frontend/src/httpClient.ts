import {defaultConfig} from "./config/default.config";
import {Config} from "./config/config";


export class Api {
    private headers: Record<string, string>;

    constructor(private config: Config) {
        this.headers = {
            "Content-type": "application/json",
            ...config.headers,
        }
    }

    get = (url: string): Promise<any> => {
        return fetch(this.config.baseUrl + url, {
            method: "GET",
            headers: this.headers,
            }).then(response => response.json())
    }

    post = (url: string, data: any): Promise<any> => {
        return fetch(this.config.baseUrl + url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: this.headers,
        }).then(response => response.json())
    }
}

export const api = new Api(defaultConfig)