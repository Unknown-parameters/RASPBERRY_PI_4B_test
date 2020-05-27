%加载数据和数据可视化
XTrain=gun2;
YTrain=gun2table;
figure
plot(XTrain{1}')
xlabel("Time Step")
title("Training Observation 1")
numFeatures = size(XTrain{1},1);
legend("Feature " + string(1:numFeatures),'Location','northeastoutside')

%训练数据的拆分和填充
%防止过多的填充对数据排序
%获取每个观测值的序列长度
numObservations = numel(XTrain);
for i=1:numObservations
    sequence = XTrain{i};
    sequenceLengths(i) = size(sequence,2);
end

%按序列长度对数据进行排序
[sequenceLengths,idx] = sort(sequenceLengths);
XTrain = XTrain(idx);
YTrain = YTrain(idx);

%在条形图中查看排序的序列长度
figure
bar(sequenceLengths)
ylim([0 30])
xlabel("Sequence")
ylabel("Length")
title("Sorted Data")


%选择小批量的大小为6，
miniBatchSize = 6;
%定义LSTM网络结构
%将输入大小指定为序列大小 15（输入数据的维度）
%指定具有 100 个隐含单元的双向 LSTM 层
%并输出序列的最后一个元素。最后，通过包含大小为 2的全连接层
%后跟 softmax 层和分类层，来指定两个类
inputSize = 15;
numHiddenUnits = 100;
numClasses = 2;

layers = [ ...
    sequenceInputLayer(inputSize)
    bilstmLayer(numHiddenUnits,'OutputMode','last')
    fullyConnectedLayer(numClasses)
    softmaxLayer
    classificationLayer]


%训练的部署
maxEpochs = 1000;
miniBatchSize = 6;


options = trainingOptions('adam', ...
    'ExecutionEnvironment','auto', ...
    'GradientThreshold',1, ...
    'MaxEpochs',maxEpochs, ...
    'MiniBatchSize',miniBatchSize, ...
    'SequenceLength','longest', ...
    'Shuffle','never', ...
    'Verbose',0, ...
    'Plots','training-progress');

%启动训练
net = trainNetwork(XTrain,YTrain,layers,options);