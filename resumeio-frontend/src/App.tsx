import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import {api} from "./httpClient";

function App() {
    const [val, setVal] = useState<[any]>()
    useEffect(() => {
        api.get("resumes/").then(
            r => {
                console.log(r)
                setVal(r)
            }
        )
    }, [])

    return (
        <div className="App">
            <header className="App-header">
                {val?.map((x: any) =>
                    (
                        <div>{x.id} - {x.name}</div>
                    ))}
                <img src={logo} className="App-logo" alt="logo"/>
                <p>
                    <code>src/App.tsx</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App;
