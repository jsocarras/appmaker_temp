import React, { useEffect, useState } from 'react';

import './navbar.css';


const Navbar = () => {

    const [pageUrl] = useState(window.location.href);
    const [pageTitle, setPageTitle] = useState('')
    const [pageHelp, setPageHelp] = useState('')

    useEffect(() => {
        if(pageUrl.includes("CloneGPT")){
            setPageTitle("CloneGPT");
            setPageHelp('This is Clone GPT ask it anything you want');
        } else if(pageUrl.includes("DebateGPT")){
            setPageTitle("Debate Bot")
            setPageHelp('Have a debate to test your knowledge!');
        } else if(pageUrl.includes("InterviewGPT")){
            setPageTitle("InterviewGPT")
            setPageHelp('Generate interview questions');
        } else if(pageUrl.includes("pdfGPT")){
            setPageTitle("PDF Chat")
            setPageHelp('This is PDF GPT upload a file and ask it anything about that file');
        } else if(pageUrl.includes("readme")){
            setPageTitle("README Generator")
            setPageHelp('Select your projects repo and have the readme generator for you after just a few questions!');
        } else {
            setPageTitle("Creospan Projects")
        }
    }, [pageUrl]);


    return (
        <>
            <nav className="navbar bg-body-tertiary fixed-top border-bottom border-body" data-bs-theme="dark">
                <div className="container-fluid">
                    <ul className='navbar-nav d-flex flex-row align-items-center justify-content-between w-100'>
                        <li>
                            {pageTitle === "Creospan Projects" ? 
                            (
                                <img src="https://creospan.com/wp-content/uploads/2022/08/creospan_logo_icon_500.png" alt="Creospan Logo" id="logo-img" height="75" width="75"></img>
                            ) : 
                            (
                                <button type="button" className="btn btn-outline-info m-3" data-bs-toggle="modal" data-bs-target="#helpModal">?</button>
                            )}
                        </li>
                        <li>
                            <h1 className='align-middle page-title'>{pageTitle}</h1>
                        </li>
                        <li>
                            <button className="navbar-toggler mx-4" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                                <span className="navbar-toggler-icon"></span>
                                 </button>
                        </li>
                    </ul>
                    <div className="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                        <div className="offcanvas-header">
                            <h5 className="offcanvas-title" id="offcanvasNavbarLabel">Navigation</h5>
                            <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                        <div className="offcanvas-body">
                            <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                                <li className="nav-item">
                                    <a className="nav-link" href="/">Home</a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" href="/CloneGPT">CloneGPT</a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" href="/readme">README Generator</a>
                                </li>
                                <li className="nav-item dropdown">
                                    <a className="nav-link dropdown-toggle" href="/InterviewGPT" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        Training / Interview Tools
                                    </a>
                                    <ul class ="dropdown-menu features-list">
                                        <li className="features-list-item">
                                            <a className="nav-link" href="/InterviewGPT">Interview GPT</a>
                                        </li>
                                        <li className="features-list-item">
                                            <a className="nav-link" href="/DebateGPT">Debate Bot</a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="nav-item dropdown">
                                    <a className="nav-link dropdown-toggle" href="/InterviewGPT" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        Vendor / Accounting Tools
                                    </a>
                                    <ul class ="dropdown-menu features-list">
                                        <li className="features-list-item">
                                            <a className="nav-link" href="/pdfGPT">PDF GPT</a>
                                        </li>
                                        <li className="features-list-item">More Coming Soon!</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
            <div className="modal fade" id="helpModal" tabindex="-1" aria-labelledby="helpModalLabel" aria-hidden="true">
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h1 className="modal-title fs-5" id="helpModalLabel">{pageTitle} Help</h1>
                            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div className="modal-body">
                                {pageHelp}
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
      </>
    );
}

export default Navbar;
