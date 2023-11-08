import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';
import CalculatorPage from "./component/CalculatorPage";

test('renders both titles', () => {
  render(<App />);
  const h1 = screen.getByText(/Examen Intra/i);
  expect(h1).toBeInTheDocument();
  const h3 = screen.getByText(/Calculatrice web/i);
  expect(h3).toBeInTheDocument();
});