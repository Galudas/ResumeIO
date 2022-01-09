import { prodConfig } from "./prod.config"
import { devConfig } from "./dev.config"

export const defaultConfig = process.env.NODE_ENV === "production"
    ? prodConfig
    : devConfig


export const defaultConfig2 = process.env.NODE_ENV === "production" ? prodConfig : devConfig


export const defaultConfig3 = process.env.NODE_ENV === "production"
    ? prodConfig
    : devConfig