import { HOST } from "../static/constant.js";

const actionBtn = document.querySelector(".action-btn");

async function logJSONData() {
  try {
    const response = await fetch(`${HOST}/patient/medical_records`);
    const jsonData = await response.json();
    if (jsonData) {
      actionBtn.innerHTML = `
                      <div class="d-grid gap-2">
                          <button type="button" class="btn btn-danger pull-right mr-3 delete">Xóa thông tin</button>
                      </div>`;
      showData(jsonData.medical_records);

      const deleteBtn = document.querySelector(".delete");
      const deleteNote = () => {
        fetch(`${HOST}/patient-management/views/delete`, {
          method: "DELETE",
        }).then((res) => (window.location.href = "/form"));
      };
      if (deleteBtn) {
        deleteBtn.onclick = () => {
          if (confirm("Bạn có muốn xóa tất cả dữ liệu đã nhập?")) {
            deleteNote();
          }
        };
      }
    }
  } catch (error) {
    console.log(error);
  }
}
logJSONData();

const $ = document.querySelector.bind(document);
const fullname = $("td#fullname");
const age = $("td#age");
const gender = $("td#gender");
const hypertension = $("td#hypertension");
const heart_disease = $("td#heart_disease");
const ever_married = $("td#ever_married");
const residence_type = $("td#residence_type");
const work_type = $("td#work_type");
const smoking_status = $("td#smoking_status");
const avg_glucose_level = $("td#avg_glucose_level");
const bmi = $("td#bmi");
const stroke = $("td#stroke");
const percentageStrokeElement = $("#percentageStroke");
const showPredictTitle = $(".show-predict-title");

const glucoseAdvices = $("#glucose-advices");
const bmiAdvices = $("#bmi-advices");
const ageAdvices = $("#age-advices");

const showData = (data) => {
  if (data) {
    fullname.innerHTML = `${data.fullname}`;
    age.innerHTML = `${data.age}`;
    gender.innerHTML = `${data.gender}`;
    hypertension.innerHTML = `${data.hypertension ? "Có" : "Không"}`;
    heart_disease.innerHTML = `${data.heart_disease ? "Có" : "Không"}`;
    ever_married.innerHTML = `${data.ever_married ? "Đã kết hôn" : "Chưa kết hôn"}`;
    residence_type.innerHTML = `${data.residence_type}` ? "Thành thị" : "Nông thôn";
    showPredictTitle.innerHTML =
      `<p class="mb-sm-3">Đã dự đoán xong</p><p>` +
      `${
        data.stroke
          ? "<h3 class='text-danger'>Bạn có nguy cơ bị đột quỵ❗</h3>"
          : "<h3 class='text-success'>Bạn không có nguy cơ bị đột quỵ ❤️</h3>"
      }` +
      `Tỉ lệ nguy cơ bị đột quỵ của bạn là:</p>`;
    percentageStrokeElement.innerText = parseFloat(data.percentageStroke).toFixed(2) + "%";

    switch (`${data.work_type}`) {
      case "govt_job":
        work_type.innerHTML = "Công việc nhà nước";
        break;
      case "privated":
        work_type.innerHTML = "Tư nhân";
        break;
      case "children":
        work_type.innerHTML = "Còn đi học/trẻ em";
        break;
      case "never_worked":
        work_type.innerHTML = "Chưa đi làm";
        break;
      case "self_employed":
        work_type.innerHTML = "Làm việc tự do";
        break;
    }

    switch (`${data.smoking_status}`) {
      case "formerly_smoked":
        smoking_status.innerHTML = "Đã từng hút trước đây";
        break;
      case "never_smoked":
        smoking_status.innerHTML = "Chưa từng hút thuốc";
        break;
      case "smokes":
        smoking_status.innerHTML = "Đang hút thuốc";
        break;
    }

    avg_glucose_level.innerHTML = `${data.avg_glucose_level}`;
    bmi.innerHTML = `${data.bmi}`;
    stroke.innerText = `${
      data.stroke
        ? "Bạn có nguy cơ bị đột quỵ, hãy nhận thêm các lời khuyên từ bác sĩ❗"
        : "Bạn không có nguy cơ bị đột quỵ, hãy tiếp tục giữ gìn sức khỏe tốt ❤️"
    }`;

    if (data.avg_glucose_level <= 90) {
      glucoseAdvices.innerText = `Mức đường huyết của bạn thấp. Hãy ăn các bữa ăn cân bằng, không nên nhịn ăn. Bổ sung thêm chất xơ và protein để ổn định lượng đường.`;
    } else if (data.avg_glucose_level > 90 && data.avg_glucose_level < 160) {
      glucoseAdvices.innerText = `Mức đường huyết của bạn lý tưởng. Bạn đang có mức đường lý tưởng! Hãy duy trì chế độ ăn lành mạnh và tập thể dục thường xuyên.`;
    } else if (data.avg_glucose_level >= 160 && data.avg_glucose_level < 230) {
      glucoseAdvices.innerText = `Mức đường huyết của bạn cao. Hãy hạn chế đường, tinh bột và carb trong bữa ăn. Tăng cường rau xanh, protein để giảm lượng đường`;
    } else if (data.avg_glucose_level >= 230) {
      glucoseAdvices.innerText = `Mức đường huyết của bạn rất cao. Cần điều trị bằng thuốc và thay đổi chế độ ăn uống ngay lập tức. Hạn chế đường hoàn toàn và chia nhỏ bữa ăn.`;
    }

    if (data.bmi <= 18) {
      bmiAdvices.innerText = `Bạn đang thiếu cân. Cần tăng cân lành mạnh bằng cách ăn nhiều calo, protein, chất béo lành mạnh hơn. Tập các bài tập tăng cơ`;
    } else if (data.bmi > 18 && data.bmi <= 25) {
      bmiAdvices.innerText = `Bạn đang ở mức cân nặng lý tưởng! Hãy duy trì chế độ ăn uống cân bằng và tập luyện thể dục đều đặn.`;
    } else if (data.bmi > 25 && data.bmi < 30) {
      bmiAdvices.innerText = `Bạn đang thừa cân! Cần giảm cân từ từ và lành mạnh bằng cách ăn nhiều rau xanh, trái cây, protein thực vật. Hạn chế đường, mỡ và carb tinh chế.`;
    } else if (data.bmi >= 30) {
      bmiAdvices.innerText = `Bạn đang béo phì! Cần giảm cân đáng kể bằng chế độ ăn kiêng lành mạnh và tập luyện thể dục thường xuyên. Nên tham khảo ý kiến bác sĩ.`;
    }

    if (data.age <= 13) {
        ageAdvices.innerText = `Bạn thuộc nhóm tuổi trẻ em. Khả năng đột quỵ rất thấp. Cần có chế độ dinh dưỡng đầy đủ và hoạt động thể chất phù hợp.`
    } else if (data.age > 13 && data.age <= 18) {
        ageAdvices.innerText = `Bạn thuộc nhóm tuổi thiếu niên. Khả năng đột quỵ thấp. Tránh căng thẳng, không hút thuốc lá, uống rượu bia. Tập thể dục thường xuyên.`
    } else if (data.age > 18 && data.age <= 45) {
        ageAdvices.innerText = `Bạn thuộc nhóm tuổi trưởng thành. Khả năng đột quỵ tăng dần theo tuổi tác. Giữ cân nặng ổn định, không hút thuốc, kiểm tra sức khỏe định kỳ.`
    } else if (data.age > 45 && data.age <= 60) {
        ageAdvices.innerText = `Bạn thuộc nhóm tuổi trung niên. Khả năng đột quỵ tăng cao hơn. Cần kiểm soát huyết áp, mỡ máu và luyện tập thể dục thường xuyên.`
    } else if (data.age >= 60) {
        ageAdvices.innerText = `Bạn thuộc nhóm cao tuổi. Khả năng đột quỵ rất cao. Cần khám sức khỏe định kỳ, kiêng rượu bia, hút thuốc. Chế độ ăn uống lành mạnh, luyện tập nhẹ nhàng.`
    } 
  }

  // 3D Chart
  // Themes begin
  am4core.useTheme(am4themes_animated);
  // Themes end
  // Create chart instance
  var chart = am4core.create("chartdiv", am4charts.XYChart3D);
  // Add data
  chart.data = [
    {
      predict: "Đột quỵ",
      strokePercentage: data.percentageStroke.toFixed(2),
    },
    {
      predict: "Bình thường",
      strokePercentage: 100 - data.percentageStroke.toFixed(2),
    },
  ];

  // Create axes
  let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
  categoryAxis.dataFields.category = "predict";
  categoryAxis.renderer.labels.template.rotation = 270;
  categoryAxis.renderer.labels.template.hideOversized = false;
  categoryAxis.renderer.minGridDistance = 20;
  categoryAxis.renderer.labels.template.horizontalCenter = "right";
  categoryAxis.renderer.labels.template.verticalCenter = "middle";
  categoryAxis.tooltip.label.rotation = 270;
  categoryAxis.tooltip.label.horizontalCenter = "right";
  categoryAxis.tooltip.label.verticalCenter = "middle";

  let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  valueAxis.title.text = "Phần trăm dự đoán đột quỵ (%)";
  valueAxis.title.fontWeight = "bold";

  // Create series
  var series = chart.series.push(new am4charts.ColumnSeries3D());
  series.dataFields.valueY = "strokePercentage";
  series.dataFields.categoryX = "predict";
  series.name = "strokePercentage";
  series.tooltipText = "{categoryX}: [bold]{valueY}%[/]";
  series.columns.template.fillOpacity = 0.8;

  var columnTemplate = series.columns.template;
  columnTemplate.strokeWidth = 2;
  columnTemplate.strokeOpacity = 1;
  columnTemplate.stroke = am4core.color("#FFFFFF");

  columnTemplate.adapter.add("fill", (fill, target) => {
    return chart.colors.getIndex(target.dataItem.index);
  });

  columnTemplate.adapter.add("stroke", (stroke, target) => {
    return chart.colors.getIndex(target.dataItem.index);
  });

  chart.cursor = new am4charts.XYCursor();
  chart.cursor.lineX.strokeOpacity = 0;
  chart.cursor.lineY.strokeOpacity = 0;

  // Gauge Chart
  window.feedAge = function (callback) {
    var tick = {};
    tick.plot0 = parseFloat(data.age);
    callback(JSON.stringify(tick));
  };

  window.feedBmi = function (callback) {
    var tick = {};
    tick.plot0 = parseFloat(data.bmi);
    callback(JSON.stringify(tick));
  };

  window.feedGlucose = function (callback) {
    var tick = {};
    tick.plot0 = parseFloat(data.avg_glucose_level);
    callback(JSON.stringify(tick));
  };

  var bmiConfig = {
    type: "gauge",
    globals: {
      fontSize: 25,
    },
    plotarea: {
      marginTop: 80,
    },
    plot: {
      size: "100%",
      valueBox: {
        placement: "center",
        text: "%v", //default
        fontSize: 35,
        rules: [
          {
            rule: "%v >= 30",
            text: "%v<br>Béo phì",
          },
          {
            rule: "%v < 30 && %v > 25",
            text: "%v<br>Thừa cân",
          },
          {
            rule: "%v < 25 && %v > 18",
            text: "%v<br>Lý tưởng",
          },
          {
            rule: "%v <  18",
            text: "%v<br>Thiếu cân",
          },
        ],
      },
    },
    tooltip: {
      borderRadius: 5,
    },
    scaleR: {
      aperture: 180,
      minValue: 0,
      maxValue: 83,
      step: 5,
      center: {
        visible: false,
      },
      tick: {
        visible: false,
      },
      item: {
        offsetR: 0,
        rules: [
          {
            rule: "%i == 9",
            offsetX: 15,
          },
        ],
      },
      labels: ["0", "30"],
      ring: {
        size: 50,
        rules: [
          {
            rule: "%v <= 18",
            backgroundColor: "#E53935",
          },
          {
            rule: "%v > 18 && %v < 25",
            backgroundColor: "#EF5350",
          },
          {
            rule: "%v >= 25 && %v < 30",
            backgroundColor: "#FFA726",
          },
          {
            rule: "%v >= 30",
            backgroundColor: "#29B6F6",
          },
        ],
      },
    },
    refresh: {
      type: "feed",
      transport: "js",
      url: "feedBmi()",
      interval: 1500,
      resetTimeout: 1000,
    },
    series: [
      {
        values: [0], // starting value
        backgroundColor: "black",
        indicator: [5, 5, 5, 5, 0.75],
        animation: {
          effect: 2,
          method: 1,
          sequence: 4,
          speed: 1000,
        },
      },
    ],
  };

  var ageConfig = {
    type: "gauge",
    globals: {
      fontSize: 25,
    },
    plotarea: {
      marginTop: 80,
    },
    plot: {
      size: "100%",
      valueBox: {
        placement: "center",
        text: "%v", //default
        fontSize: 35,
        rules: [
          {
            rule: "%v >= 60",
            text: "%v<br>Cao tuổi",
          },
          {
            rule: "%v < 60 && %v > 45",
            text: "%v<br>Trung niên",
          },
          {
            rule: "%v < 45 && %v > 18",
            text: "%v<br>Trưởng thành",
          },
          {
            rule: "%v < 18 && %v > 13",
            text: "%v<br>Thiếu niên",
          },
          {
            rule: "%v < 13 && %v > 0",
            text: "%v<br>Trẻ em",
          },
        ],
      },
    },
    tooltip: {
      borderRadius: 5,
    },
    scaleR: {
      aperture: 180,
      minValue: 0,
      maxValue: 150,
      step: 5,
      center: {
        visible: false,
      },
      tick: {
        visible: false,
      },
      item: {
        offsetR: 0,
        rules: [
          {
            rule: "%i == 9",
            offsetX: 15,
          },
        ],
      },
      labels: ["0", "150"],
      ring: {
        size: 50,
        rules: [
          {
            rule: "%v <= 13",
            backgroundColor: "#E53935",
          },
          {
            rule: "%v > 13 && %v < 18",
            backgroundColor: "#EF5350",
          },
          {
            rule: "%v >= 18 && %v < 45",
            backgroundColor: "#FFA726",
          },
          {
            rule: "%v >= 45 && %v < 60",
            backgroundColor: "#29B6F6",
          },
          {
            rule: "%v >= 60",
            backgroundColor: "#0f1963",
          },
        ],
      },
    },
    refresh: {
      type: "feed",
      transport: "js",
      url: "feedAge()",
      interval: 1500,
      resetTimeout: 1000,
    },
    series: [
      {
        values: [0], // starting value
        backgroundColor: "black",
        indicator: [5, 5, 5, 5, 0.75],
        animation: {
          effect: 2,
          method: 1,
          sequence: 4,
          speed: 1000,
        },
      },
    ],
  };

  var glucoseConfig = {
    type: "gauge",
    globals: {
      fontSize: 25,
    },
    plotarea: {
      marginTop: 80,
    },
    plot: {
      size: "100%",
      valueBox: {
        placement: "center",
        text: "%v", //default
        fontSize: 35,
        rules: [
          {
            rule: "%v >= 230",
            text: "%v<br>Béo phì",
          },
          {
            rule: "%v < 230 && %v > 160",
            text: "%v<br>Thừa cân",
          },
          {
            rule: "%v < 160 && %v > 90",
            text: "%v<br>Lý tưởng",
          },
          {
            rule: "%v <=  90",
            text: "%v<br>Thiếu cân",
          },
        ],
      },
    },
    tooltip: {
      borderRadius: 5,
    },
    scaleR: {
      aperture: 180,
      minValue: 0,
      maxValue: 380,
      step: 100,
      center: {
        visible: false,
      },
      tick: {
        visible: false,
      },
      item: {
        offsetR: 0,
        rules: [
          {
            rule: "%i == 9",
            offsetX: 15,
          },
        ],
      },
      labels: ["0", "90", "160", "230"],
      ring: {
        size: 50,
        rules: [
          {
            rule: "%v <= 90",
            backgroundColor: "#E53935",
          },
          {
            rule: "%v > 90 && %v < 160",
            backgroundColor: "#EF5350",
          },
          {
            rule: "%v >= 160 && %v < 230",
            backgroundColor: "#FFA726",
          },
          {
            rule: "%v >= 230",
            backgroundColor: "#29B6F6",
          },
        ],
      },
    },
    refresh: {
      type: "feed",
      transport: "js",
      url: "feedGlucose()",
      interval: 1500,
      resetTimeout: 1000,
    },
    series: [
      {
        values: [0], // starting value
        backgroundColor: "black",
        indicator: [5, 5, 5, 5, 0.75],
        animation: {
          effect: 2,
          method: 1,
          sequence: 4,
          speed: 1000,
        },
      },
    ],
  };
  zingchart.render({
    id: "ageChart",
    data: ageConfig,
    height: "350",
    width: "100%",
  });
  zingchart.render({
    id: "bmiChart",
    data: bmiConfig,
    height: "350",
    width: "100%",
  });
  zingchart.render({
    id: "glucoseChart",
    data: glucoseConfig,
    height: "350",
    width: "100%",
  });
};
