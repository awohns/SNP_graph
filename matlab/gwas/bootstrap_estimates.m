function estimate = bootstrap_estimates(est,refAnnot,noIter)
%UNTITLED10 Summary of this function goes here
%   Detailed explanation goes here
if nargin < 3
    noIter = 1000;
end
if nargin < 2
    refAnnot = 1;
end

estimate = combine_estimates(est, refAnnot);
for iter = 1:noIter
    ii = randsample(1:length(est),length(est),true);
    bootstrap(ii) = combine_estimates(est(ii), refAnnot);
end

estimate.enrichmentSE = std(vertcat(bootstrap.enrichment));
estimate.enrichmentZ = (estimate.enrichment-1)./estimate.enrichmentSE;
estimate.h2SE = std(vertcat(bootstrap.h2));
estimate.h2Z = estimate.h2./estimate.h2SE;
estimate.paramsSE = std(horzcat(bootstrap.params)')';
estimate.paramsZ = estimate.params./estimate.paramsSE;

end

