import React, {Fragment, useEffect, useState} from 'react';
import {InputTextarea} from "primereact/inputtextarea";
import {Button} from "primereact/button";
import {InputText} from "primereact/inputtext";
import {Card} from "primereact/card";
import {api} from "./httpClient";
import {DataTable} from "primereact/datatable";
import {Column} from "primereact/column";

function App() {
    const [jobDescription, setJobDescription] = useState<any>("")
    const [candidateDescription, setCandidateDescription] = useState<any>("")
    const [userName, setUserName] = useState<any>("")
    const [isAnalyzed, setIsAnalyzed] = useState<boolean>(false)
    const [isShown, setIsShown] = useState<boolean>(false)
    const [score, setScore] = useState<any>(null)
    const [tableData, setDataTableData] = useState<any>([])

    const handleSubmit = (e: any) => {
        e.preventDefault()
        console.log("This is value ", jobDescription, candidateDescription)
        setIsShown(true)
        api.post("matching",
            {"jobDescription": jobDescription, "candidateDescription": candidateDescription, "candidateName": userName})
            .then(r => {
                setScore(r["score"])
                setIsAnalyzed(true)
            })
    }

    useEffect(() => {
        api.get("matching")
            .then(r => setDataTableData(r))
    }, [])

    const reload = (e: any) => {
        e.preventDefault()
        window.location.reload()
    }

    return (
        <Fragment>
            <form onSubmit={handleSubmit}>
                <div className={"p-text-center"}>
                    <div style={{fontSize: "40px"}}>ResumeIO</div>
                    <div style={{fontSize: "20px"}}>Analyze your cv info to match job.</div>

                    <h5>Candidate Name</h5>
                    <InputText value={userName} onChange={(e) => setUserName(e.target.value)}/>
                    <div style={{display: "flex", justifyContent: "center"}}>

                        <div style={{display: "block", marginRight: "20px"}}>
                            <h5>Job Description</h5>

                            <InputTextarea
                                rows={20}
                                cols={50}
                                value={jobDescription}
                                onChange={(e) => {
                                    setJobDescription(e.target.value)
                                }}
                                autoResize/>
                        </div>
                        <div style={{display: "block", marginLeft: "20px"}}>

                            <h5>Candidate Description</h5>
                            <InputTextarea
                                rows={20}
                                cols={50}
                                value={candidateDescription}
                                onChange={(e) => {
                                    setCandidateDescription(e.target.value)
                                }}
                                autoResize/>
                        </div>
                    </div>
                    <Button style={{marginTop: "25px"}} label="Compare" className="p-button-success" type={"submit"}/>
                    {isShown && (isAnalyzed ?
                        <div style={{display: "flex", justifyContent: "center", marginTop: "20px"}}>
                            <Card title={userName}
                                  style={{width: '25rem', marginBottom: '2em', border: "2px solid green"}}>
                                <p className="p-m-0" style={{lineHeight: '1.5'}}>Candidate score: {score}</p>
                                <Button style={{marginTop: "25px"}} label="Cancel" className="p-button-danger"
                                        onClick={reload}/>
                            </Card>
                        </div>
                        :
                        <div style={{display: "flex", justifyContent: "center", marginTop: "20px"}}>
                            <div className="lds-ring">
                                <div/>
                                <div/>
                                <div/>
                                <div/>
                            </div>
                        </div>)
                    }
                    <div style={{fontSize: "20px", marginTop: "30px"}}>Results</div>
                    <div className="card" style={{display: "flex", justifyContent: "center", paddingTop: "20px"}}>

                        <DataTable value={tableData} responsiveLayout="scroll"
                                   style={{width: "20%", border: "2px solid black"}}>
                            <Column field="name" header="Name"/>
                            <Column field="score" header="Score"/>
                        </DataTable>


                    </div>
                </div>

            </form>
        </Fragment>
    );
}

export default App;
