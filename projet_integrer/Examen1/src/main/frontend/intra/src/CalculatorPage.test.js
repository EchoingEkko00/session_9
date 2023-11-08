import React from 'react';
import {render, fireEvent, screen, waitFor} from '@testing-library/react';
import CalculatorPage from './component/CalculatorPage';
import CalcService from './service/CalcService';
import {act} from "react-dom/test-utils";

jest.mock('./service/CalcService'); // Mock the service

test('renders all my input', () => {
    render(<CalculatorPage />);
    const one = screen.getAllByPlaceholderText(/One/i);
    expect(one[0]).toBeInTheDocument();
    expect(one[1]).toBeInTheDocument();
    const two = screen.getAllByPlaceholderText(/Two/i);
    expect(two[0]).toBeInTheDocument();
    expect(two[1]).toBeInTheDocument();
});

test('renders all my button', () => {
    render(<CalculatorPage />);
    const submit = screen.getAllByRole('button');
    expect(submit[0]).toBeInTheDocument();
    expect(submit[1]).toBeInTheDocument();
});

describe('CalculatorPage', () => {
    it('should render the component', () => {
        render(<CalculatorPage />);

        // Ensure that the component is rendered
        const oneInput = screen.getAllByPlaceholderText('One');
        const twoInput = screen.getAllByPlaceholderText('Two');
        const addButton = screen.getByText('Additionne');
        const subtractButton = screen.getByText('Soustrait');

        expect(oneInput[0]).toBeInTheDocument();
        expect(twoInput[0]).toBeInTheDocument();
        expect(oneInput[1]).toBeInTheDocument();
        expect(twoInput[1]).toBeInTheDocument();
        expect(addButton).toBeInTheDocument();
        expect(subtractButton).toBeInTheDocument();
    });

    it('should perform addition correctly', async () => {
        const { getByLabelText, getByText } = render(<CalculatorPage />);

        // Mock the service response
        CalcService.add.mockResolvedValue({ result: 5 });

        // Get input fields and the add button
        const oneInput = screen.getAllByPlaceholderText('One');
        const twoInput = screen.getAllByPlaceholderText('Two');
        const addButton = screen.getByText('Additionne');

        // Enter values and trigger the addition
        fireEvent.change(oneInput[0], { target: { value: '2' } });
        fireEvent.change(twoInput[0], { target: { value: '3' } });
        fireEvent.click(addButton);

        // Get the result element
        const resultSub = await screen.findByText(/5/i); // Adjust the text as needed

        expect(resultSub).toBeInTheDocument();
    });

    it('should perform subtraction correctly', async () => {
        render(<CalculatorPage />);

        CalcService.sub.mockResolvedValue({ result: 3 });

        // Get input fields and the subtract button
        const oneInput = screen.getAllByPlaceholderText('One');
        const twoInput = screen.getAllByPlaceholderText('Two');
        const subtractButton = screen.getByText('Soustrait');

        // Enter values and trigger the subtraction
        fireEvent.change(oneInput[1], { target: { value: '5' } });
        fireEvent.change(twoInput[1], { target: { value: '2' } });
        fireEvent.click(subtractButton);

        //Wait for the result element to be rendered
        const resultSub = await screen.findByText(/3/i); // Adjust the text as needed

        expect(resultSub).toBeInTheDocument();
    });
});
