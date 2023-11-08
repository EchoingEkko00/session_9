import React, {useState} from 'react';
import CalcService from '../service/CalcService.js'

const CalculatorPage = (props) => {
    const [one, setOne] = useState('')
    const [two, setTwo] = useState('')
    const [resultAdd, setResultAdd] = useState('')
    const [oneSub, setOneSub] = useState('')
    const [twoSub, setTwoSub] = useState('')
    const [resultSub, setResultSub] = useState('')

    const onSubmit = async (e) => {
        e.preventDefault()

        if (!one || !two) {
            alert('Requiert 2 nombres')
            return
        }
        await CalcService.add(one, two, setResultAdd)
        console.log(resultAdd)
        setOne('')
        setTwo('')
    }

    const onSubmitSubstract = async (e) => {
        e.preventDefault()

        if (!oneSub || !twoSub) {
            alert('Requiert 2 nombres')
            return
        }
        await CalcService.sub(oneSub, twoSub, setResultSub)
        setOneSub('')
        setTwoSub('')
    }

    return (
        <>
            <form className='add-form' onSubmit={onSubmit}>
                <div className='form-control'>
                    <label>One</label>
                    <input type='number' placeholder='One'
                           value={one}
                           onChange={(e) => setOne(e.target.value)}/>
                </div>
                <div className='form-control'>
                    <label>Two</label>
                    <input type='number' placeholder='Two'
                           value={two}
                           onChange={(e) => setTwo(e.target.value)}/>
                </div>
                <input type='submit' value='Additionne' className='btn btn-block'/>
                <h1>{resultAdd}</h1>
            </form>
            <br/><br/>
            <form className='add-form' onSubmit={onSubmitSubstract}>
                <div className='form-control'>
                    <label>One</label>
                    <input type='number' placeholder='One'
                           value={oneSub}
                           onChange={(e) => setOneSub(e.target.value)}/>
                </div>
                <div className='form-control'>
                    <label>Two</label>
                    <input type='number' placeholder='Two'
                           value={twoSub}
                           onChange={(e) => setTwoSub(e.target.value)}/>
                </div>
                <input type='submit' value='Soustrait' className='btn btn-block'/>
                <h1>{resultSub}</h1>
            </form>
        </>
    );
}

export default CalculatorPage;