import { ColourPicker } from "./components/ColourPicker";
import { Header } from "./components/navbar/Header";
import "./styles/App.css";

export const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <ColourPicker />
      </header>
    </div>
  );
};
