import React, { useState } from "react";

function SearchForm({ ad, setAd }) {
  const [validationErrors, setValidationErrors] = useState(""); //state of input validation

  function handleChangeProduct(e) {
    const { value } = e.target;
    setAd(value);

    if (!value.length) {
      setValidationErrors("Keyword required");
    } else {
      return setValidationErrors("");
    }
  }
  return (
    <div className="searchForm searchForm__container">
      <input
        className="searchForm__input"
        placeholder="Search"
        type="text"
        name="text"
        value={ad}
        minLength="1"
        required
        onChange={handleChangeProduct}
      />
      <div className={`input-hidden ${validationErrors ? "input-error" : ""}`}>
        {validationErrors}
      </div>
    </div>
  );
}

export default SearchForm;
