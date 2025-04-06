import React, { useState } from "react";
import './component.scss';
import axios from "axios";
import { useNavigate } from "react-router-dom";
import './Patientdata.css';

const Patient = () => {
  const navigate = useNavigate();
  const [patientdata, setPatient] = useState({
    name: "",
    email: "",
    dob: "",
    state: "",
    phone_number: "",
    gender: "",
    location: "",
    image: null,
    model_type: "InceptionV3", // Default model
  });

  const setVal = (event) => {
    const { name, value } = event.target;
    setPatient((prev) => ({ ...prev, [name]: value }));
  };

  const setImage = (event) => {
    setPatient((prev) => ({
      ...prev,
      image: event.target.files[0],
    }));
  };

  const predict = async (e) => {
    e.preventDefault();
    const patientformdata = new FormData();
    Object.keys(patientdata).forEach((key) => {
      patientformdata.append(key, patientdata[key]);
    });

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/patient/", patientformdata);
      if (response.status === 201) {
        alert("Patient details added successfully");
        navigate("/patientdata");
      } else {
        alert("Error: " + response.status);
      }
    } catch (error) {
      alert("Invalid credentials or error in submission");
    }
  };

  return (
    <section className="vh-90 mb-4">
      <div className="container h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-xl-9">
            <h1 className="text-primary mb-4">Fill Patient Health Details</h1>

            <div id="car" className="car">
              <div className="card-body text-primary">
                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Full Name</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input type="text" name="name" className="form-control" value={patientdata.name} onChange={setVal} />
                  </div>
                </div>

                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Email ID</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input type="email" name="email" className="form-control" value={patientdata.email} onChange={setVal} />
                  </div>
                </div>

                <hr className="mx-n3" />
                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Date of Birth</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input type="date" name="dob" className="form-control" value={patientdata.dob} onChange={setVal} />
                  </div>
                </div>

                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">State</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input type="text" name="state" className="form-control" value={patientdata.state} onChange={setVal} />
                  </div>
                </div>

                <hr className="mx-n3" />
                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Phone Number</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input type="text" name="phone_number" className="form-control" value={patientdata.phone_number} onChange={setVal} />
                  </div>
                </div>

                <div className="row align-items-center pt-4 pb-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Gender</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <select className="form-select" name="gender" value={patientdata.gender} onChange={setVal}>
                      <option value="" disabled>Select Gender</option>
                      <option value="male">Male</option>
                      <option value="female">Female</option>
                      <option value="other">Other</option>
                    </select>
                  </div>
                </div>

                <hr className="mx-n3" />
                <div className="row align-items-center py-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Address</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <textarea className="form-control" rows="3" placeholder="Address" name="location" value={patientdata.location} onChange={setVal}></textarea>
                  </div>
                </div>

                <div className="row align-items-center py-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Select Model</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <select className="form-select" name="model_type" value={patientdata.model_type} onChange={setVal}>
                      <option value="InceptionV3">InceptionV3</option>
                      <option value="MobileNet">MobileNet</option>
                      <option value="DenseNet">DenseNet</option>
                    </select>
                  </div>
                </div>

                <div className="row align-items-center py-3">
                  <div className="col-md-3 ps-5">
                    <h6 className="mb-0">Upload Histopathology Image</h6>
                  </div>
                  <div className="col-md-9 pe-5">
                    <input className="form-control" type="file" name="image" onChange={setImage} />
                    <div className="small text-muted mt-2 text-primary">Upload size should be less than 2MB</div>
                  </div>
                </div>

                <hr className="mx-n3" />
                <div className="px-5 py-4 center">
                  <button type="submit" className="btn nav-op" onClick={predict}>Submit</button>
                </div>

              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default Patient;
