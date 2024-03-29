import React, { useState, useEffect } from "react";
import UserForm from "../userForm/UserForm";
import useFormValidation from "../../utils/hooks/useFormValidation";

function Profile({ userInfo, handleUpdateUser }) {
  const [input, setInput] = useState("");
  const { values, handleChange, errors, isValid, setValues } =
    useFormValidation();

  function handleChangeInput(e) {
    handleChange(e);
    if (input.length > 0) {
      setInput("");
    }
  }

  function handleUpdate(e) {
    e.preventDefault();
    handleUpdateUser({
      first_name: values.first_name,
      last_name: values.last_name,
      phone: values.phone,
    });
    window.location.reload();
  }

  useEffect(() => {
    setValues(userInfo);
  }, [userInfo, setValues]);

  return (
    <UserForm
      title="Hello,"
      userName={userInfo.first_name}
      onSubmit={handleUpdate}
      buttonText="Save"
      errors={!isValid}
      disabled={!isValid}
    >
      <label className="userForm__label-profile">
        <h1 className="userForm__subtitle">First name</h1>
        <input
          value={values.first_name || ""}
          title="First name"
          name="first_name"
          type="text"
          minLength="3"
          required
          autoComplete="on"
          className="userForm__input"
          maxLength="30"
          onChange={handleChangeInput}
        />
        <div
          className={`input-hidden ${errors.first_name ? "input-error" : ""}`}
        >
          {errors.first_name}
        </div>
      </label>
      <label className="userForm__label-profile">
        <h1 className="userForm__subtitle">Surname</h1>
        <input
          value={values.last_name || ""}
          title="Surname"
          name="last_name"
          type="text"
          required
          minLength="3"
          autoComplete="on"
          className="userForm__input"
          maxLength="30"
          onChange={handleChangeInput}
        />
        <div
          className={`input-hidden ${errors.last_name ? "input-error" : ""}`}
        >
          {errors.last_name}
        </div>
      </label>
      <label className="userForm__label-profile">
        <h1 className="userForm__subtitle">Phone</h1>
        <input
          value={values.phone || ""}
          title="Phone"
          type="tel"
          name="phone"
          required
          pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"
          autoComplete="on"
          className="userForm__input"
          onChange={handleChangeInput}
        />
        <div className={`input-hidden ${errors.phone ? "input-error" : ""}`}>
          {errors.phone}
        </div>
      </label>
    </UserForm>
  );
}

export default Profile;
