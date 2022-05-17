import React, { useState } from "react";
import { SketchPicker } from "react-color";

export const ColourPicker = () => {
  const [currentColour, setColour] = useState(null);
  const [currentHex, setHex] = useState(null);
  const [state, setState] = useState({ background: "null" });

  const handleChangeComplete = async (color) => {
    setState({ background: color.hex });
    await fetch("/Guess?colour=" + color.hex.replace("#", ""))
      .then((res) => res.json())
      .then((data) => {
        setColour(data.colour_name);
        setHex(data.colour_hex);
      });
  };

  return (
    <div>
      <header>
        <div
          style={{
            backgroundColor: state.background,
            padding: "24px",
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <SketchPicker
              color={state.background}
              onChangeComplete={handleChangeComplete}
            />
          </div>
        </div>
        <div
          style={{
            backgroundColor: currentHex,
            paddingTop: "50px",
            paddingBottom: "350px",
          }}
        >
          {currentColour == null ? (
            <></>
          ) : (
            <div className="boxy">
              <p className="text-box">{currentColour}</p>
            </div>
          )}
        </div>
      </header>
    </div>
  );
};
